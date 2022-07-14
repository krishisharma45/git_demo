# syntax=docker/dockerfile:1.2
FROM python:3.8-slim

WORKDIR /workspace

ENV PYTHONUNBUFFERED=1

RUN rm -rf /etc/apt/apt.conf.d/docker-clean

RUN --mount=type=cache,mode=0777,target=/var/cache/apt apt-get update \
    && rm -rf /var/lib/apt/lists/*

COPY services/app/requirements.txt .
RUN --mount=type=cache,mode=0777,target=/root/.cache pip install --upgrade pip \
    && pip install -r requirements.txt

RUN useradd -m appuser && chown -R appuser /workspace
USER appuser

COPY . .

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
