# --- Stage 1: Build wheel with generated gRPC code ---
FROM python:3.11-slim AS builder

# Install tools
RUN pip install --upgrade pip hatch grpcio-tools

# Set up workdir and copy project files
WORKDIR /src
COPY pyproject.toml ./
COPY ./src ./src

# Compile gRPC .proto
WORKDIR /src
RUN python -m grpc_tools.protoc \
  -I./src \
  --python_out=./src/service_c \
  --grpc_python_out=./src/service_c \
  ./src/service_a.proto

RUN sed -i 's/^import service_a_pb2 as/from . import service_a_pb2 as/' src/service_c/service_a_pb2_grpc.py



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
CMD ["python", "-m", "service_c"]

