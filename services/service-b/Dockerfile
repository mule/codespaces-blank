# Dockerfile for service-b
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install .

COPY app/ ./app/

CMD ["python", "-m", "app.main"]
