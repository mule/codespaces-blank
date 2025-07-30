import grpc
from concurrent import futures
from . import service_a_pb2, service_a_pb2_grpc

class ServiceAImpl(service_a_pb2_grpc.ServiceAServicer):
    def CallService(self, request, context):
        # Simple echo implementation
        response = service_a_pb2.Response(result=f"Echo: {request.message}")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_a_pb2_grpc.add_ServiceAServicer_to_server(ServiceAImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Service A gRPC server started on port 50051")
    server.wait_for_termination()
