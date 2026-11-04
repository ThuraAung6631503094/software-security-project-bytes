# NoteVault runtime image (CFG-02 hardening).
# Base image: slim variant, no baked secret, minimal copy, non-root user.
# Before final submission, pin the base by digest for reproducibility, e.g.
#   FROM python:3.12-slim-bookworm@sha256:<digest>
# Get the current digest with:
#   docker pull python:3.12-slim-bookworm
#   docker inspect --format='{{index .RepoDigests 0}}' python:3.12-slim-bookworm
FROM python:3.12-slim-bookworm

WORKDIR /app

# Install dependencies first for better layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application code — not the whole build context, no committed files.
COPY app.py .

# Run as an unprivileged user instead of root.
RUN useradd --create-home --uid 10001 notevault
USER 10001:10001

EXPOSE 8080
CMD ["python", "app.py"]
