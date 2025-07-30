import grpc
import nats
import asyncio
from service_a_pb2 import Request, Response
from service_a_pb2_grpc import ServiceAStub

async def consume_and_call():
    # Connect to NATS
    nc = await nats.connect("nats://nats:4222")

    async def message_handler(msg):
        data = msg.data.decode()
        print(f"[Service-C] Received message: {data}")

        # Call gRPC API from service-a (optional, can be commented if not needed for test)
        # async with grpc.aio.insecure_channel("service-a:50051") as channel:
        stub = ServiceAStub(channel)
        response = await stub.CallService(Request(message=data))
        print(f"Response from service-a: {response.result}")

    # Subscribe to JetStream
    js = nc.jetstream()
    await js.subscribe("service-b-data", cb=message_handler)

    print("Service C is running and consuming messages from NATS JetStream (subject: service-b-data)")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(consume_and_call())
