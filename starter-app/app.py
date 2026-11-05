"""
NoteVault — a small team note-sharing web app + JSON API (term-project starter).

This is your TERM-PROJECT TARGET. It is a normal-looking app that contains several
realistic security weaknesses. Your job (see project/README.md): threat-model it,
find and document the vulnerabilities, fix them, and harden the build/release.

We do NOT list the vulnerabilities here — finding them is the assignment.

Run:  docker compose up   (then http://localhost:8080)
"""
import datetime
import hashlib
import hmac
import os
import sqlite3

import jwt  # PyJWT
from flask import Flask, request, jsonify, render_template_string, redirect, make_response
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
DB = "/tmp/notevault.db"
# AUTH-01 fix: the signing secret is injected at runtime, never hard-coded.
SECRET = os.environ.get("NOTEVAULT_SECRET")
if not SECRET:
    raise RuntimeError("NOTEVAULT_SECRET must be configured")

# AUTH-04 / AUTH-05 fix: Flask-WTF CSRF protection + secure session-cookie attributes.
app.config.update(
    SECRET_KEY=SECRET,
    SESSION_COOKIE_NAME="flask_session",
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE", "0") == "1",
)
csrf = CSRFProtect(app)
# The JWT auth cookie is kept separate from Flask-WTF's own session cookie.
AUTH_COOKIE = "notevault_session"

# Anti-copying: every team's build is seeded with a marker derived from their own TEAM_ID, so
# any evidence a team submits (SQLi dump, IDOR response, admin-panel screenshot) that shows the
# admin's notes carries a value traceable to exactly one team — see instructor/anti-cheating.md.
TEAM_ID = os.environ.get("TEAM_ID", "unassigned")
TEAM_SALT = os.environ.get("TEAM_SALT", "notevault-anti-copy-dev-salt")


def team_marker():
    return hmac.new(TEAM_SALT.encode(), TEAM_ID.encode(), hashlib.sha256).hexdigest()[:12]


PAGE = """
<!doctype html><title>NoteVault</title>
<h1>NoteVault</h1>
{% if user %}<p>Signed in as <b>{{ user }}</b> · <a href="/logout">logout</a>
  {% if is_admin %}· <a href="/admin">admin</a>{% endif %}</p>
<form method=post action="/notes">
  <input type=hidden name=csrf_token value="{{ csrf_token() }}">
  <input name=title placeholder=title>
  <input name=body placeholder=note><button>Add note</button></form>
<h3>Your notes</h3>
<ul>
{% for note in notes %}
  <li>#{{ note["id"] }} <b>{{ note["title"] }}</b>: {{ note["body"] }}</li>
{% endfor %}
</ul>
<form action="/search"><input name=q placeholder="search notes"><button>Search</button></form>
{% else %}
<form method=post action="/login">
  <input type=hidden name=csrf_token value="{{ csrf_token() }}">
  user <input name=username> pass <input name=password type=password>
  <button>Login</button></form>
<form method=post action="/register">
  <input type=hidden name=csrf_token value="{{ csrf_token() }}">
  new: <input name=username> <input name=password type=password>
  <button>Register</button></form>
{% endif %}
"""


def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def seed():
    con = db()
    con.executescript(
        "DROP TABLE IF EXISTS users; DROP TABLE IF EXISTS notes;"
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT);"
        "CREATE TABLE notes (id INTEGER PRIMARY KEY, owner TEXT, title TEXT, body TEXT);"
    )
    con.executemany("INSERT INTO users (username, password, role) VALUES (?,?,?)",
                    [("alice", generate_password_hash("alicepw"), "user"),
                     ("admin", generate_password_hash("admin123"), "admin")])
    con.executemany("INSERT INTO notes (owner, title, body) VALUES (?,?,?)",
                    [("alice", "groceries", "milk, eggs"),
                     ("admin", "infra", "prod db password is hunter2"),
                     ("admin", "build-tag", "team=%s marker=%s" % (TEAM_ID, team_marker()))])
    con.commit()
    con.close()


def current_user():
    # AUTH-01 fix: only HS256 is accepted ("none" removed); expiry is enforced by PyJWT.
    tok = request.cookies.get(AUTH_COOKIE, "")
    if not tok:
        return None
    try:
        data = jwt.decode(tok, SECRET, algorithms=["HS256"])
        username = data.get("sub")
        return username if isinstance(username, str) else None
    except jwt.InvalidTokenError:
        return None


def role_of(username):
    con = db()
    r = con.execute("SELECT role FROM users WHERE username = ?", (username,)).fetchone()
    con.close()
    return r["role"] if r else None


@app.route("/")
def home():
    user = current_user()
    rows = []
    if user:
        con = db()
        rows = con.execute("SELECT id,title,body FROM notes WHERE owner = ?", (user,)).fetchall()
        con.close()
    # INJ-02 fix: pass notes as structured data; Jinja auto-escaping neutralises stored HTML/JS.
    return render_template_string(PAGE, user=user, is_admin=(user and role_of(user) == "admin"),
                                  notes=rows)


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username") or (request.get_json(silent=True) or {}).get("username")
    password = request.form.get("password") or (request.get_json(silent=True) or {}).get("password")
    if not username or not password:
        return "username and password required", 400
    # AC-01 fix: the role is set by the server, never taken from the request.
    con = db()
    try:
        con.execute("INSERT INTO users (username, password, role) VALUES (?,?,?)",
                    (username, generate_password_hash(password), "user"))
        con.commit()
    except sqlite3.IntegrityError:
        # AC-02 fix: usernames are unique; a duplicate is rejected, not silently created.
        con.rollback()
        return "username already exists", 409
    finally:
        con.close()
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username") or (request.get_json(silent=True) or {}).get("username")
    password = request.form.get("password") or (request.get_json(silent=True) or {}).get("password")
    # AUTH-02 fix: parameterized lookup by username; AUTH-03 fix: verify an adaptive password hash.
    con = db()
    row = con.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    con.close()
    if not row or not check_password_hash(row["password"], password or ""):
        return "login failed", 401
    # AUTH-01 fix: HS256 token with an expiry claim.
    tok = jwt.encode(
        {"sub": username,
         "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)},
        SECRET, algorithm="HS256",
    )
    resp = make_response(redirect("/"))
    # AUTH-04 fix: HttpOnly + SameSite always; Secure when served over HTTPS.
    resp.set_cookie(
        AUTH_COOKIE, tok,
        httponly=True,
        samesite="Lax",
        secure=app.config["SESSION_COOKIE_SECURE"],
    )
    return resp


@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.delete_cookie(AUTH_COOKIE)
    return resp


@app.route("/notes", methods=["POST"])
def add_note():
    user = current_user()
    if not user:
        return "auth required", 401
    title = request.form.get("title", "")
    body = request.form.get("body", "")
    con = db()
    con.execute("INSERT INTO notes (owner,title,body) VALUES (?,?,?)", (user, title, body))
    con.commit()
    con.close()
    return redirect("/")


@app.route("/api/notes/<int:nid>")
def api_note(nid):
    user = current_user()
    if not user:
        return jsonify(error="auth required"), 401
    # AC-03 fix: constrain by note ID AND the authenticated owner.
    con = db()
    r = con.execute("SELECT id,owner,title,body FROM notes WHERE id = ? AND owner = ?",
                    (nid, user)).fetchone()
    con.close()
    return (jsonify(dict(r)) if r else (jsonify(error="not found"), 404))


@app.route("/search")
def search():
    user = current_user()
    if not user:
        return "auth required", 401
    term = request.args.get("q", "")
    # INJ-01 fix: parameterized query (owner and term are data, not SQL).
    con = db()
    rows = con.execute(
        "SELECT id,title,body FROM notes WHERE owner = ? AND body LIKE ?",
        (user, f"%{term}%"),
    ).fetchall()
    con.close()
    # INJ-03 fix: fixed template; note content is passed as data and auto-escaped (no SSTI/XSS).
    return render_template_string(
        """<a href="/">back</a><ul>
        {% for note in notes %}<li>{{ note["title"] }}: {{ note["body"] }}</li>{% endfor %}
        </ul>""",
        notes=rows,
    )


@app.route("/admin")
def admin():
    user = current_user()
    if not user or role_of(user) != "admin":
        return "forbidden", 403
    # INFO-01 fix: never serialize the password column to clients.
    con = db()
    rows = con.execute("SELECT id,username,role FROM users").fetchall()
    con.close()
    return jsonify([dict(r) for r in rows])


@app.route("/export")
def export():
    if not current_user():
        return "auth required", 401
    # INJ-04 fix: no shell. Accept only an allowlisted format; never run user input.
    fmt = request.args.get("fmt", "txt")
    if fmt != "txt":
        return "unsupported format", 400
    return "<pre>exporting notes as txt</pre>"


# CFG-01 fix: generic error responses so failures never leak internal detail.
@app.errorhandler(404)
def not_found(_):
    return "not found", 404


@app.errorhandler(500)
def server_error(_):
    return "internal server error", 500


if __name__ == "__main__":
    seed()
    # CFG-01 fix: debug disabled; host/port from the environment. The app listens on all
    # interfaces INSIDE the container, while host exposure is restricted to localhost by the
    # docker-compose port mapping (127.0.0.1:8080:8080).
    app.run(
        host=os.environ.get("NOTEVAULT_HOST", "0.0.0.0"),
        port=int(os.environ.get("NOTEVAULT_PORT", "8080")),
        debug=False,
    )
