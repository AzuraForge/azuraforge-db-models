# ========== GÜNCELLEME: dbmodels/Dockerfile ==========
# Stage 1: Builder
FROM python:3.10-slim-bullseye AS builder

RUN apt-get update && apt-get install -y git --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app/src

COPY src ./src
COPY pyproject.toml /app/
COPY setup.py /app/

RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir /app

# Stage 2: Runtime
FROM python:3.10-slim-bullseye AS runtime

WORKDIR /app/src

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app/src ./src

CMD ["python", "-c", "print('AzuraForge Databae Models built successfully!')"]