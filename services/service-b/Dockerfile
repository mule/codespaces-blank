# --- Stage 1: Build wheel with generated gRPC code ---
FROM python:3.11-slim AS builder

# Install tools
RUN pip install --upgrade pip hatch 

# Set up workdir and copy project files
WORKDIR /src
COPY pyproject.toml ./
COPY ./src ./src

# Build wheel
RUN hatch build -t wheel

# --- Stage 2: Final image with only installed package ---
FROM python:3.11-slim

WORKDIR /app

# Install the built wheel
COPY --from=builder /src/dist/*.whl ./
RUN pip install --no-cache-dir ./*.whl

# Run service from installed package
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
CMD ["python", "-m", "service_b"]

