# Dockerfile for service-c
FROM python:3.11-slim AS builder

WORKDIR /src
RUN pip install --upgrade pip hatch
COPY pyproject.toml ./
COPY service_c/ ./service_c/
WORKDIR /src/service_c
RUN pip install grpcio-tools && python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_a.proto
# Patch generated gRPC file for relative imports
RUN sed -i 's/^import service_a_pb2 as/from . import service_a_pb2 as/' service_a_pb2_grpc.py
WORKDIR /src
RUN hatch build -t wheel

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /src/dist/*.whl ./
RUN pip install --no-cache-dir ./*.whl

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
CMD ["python", "-m", "service_c.main"]
