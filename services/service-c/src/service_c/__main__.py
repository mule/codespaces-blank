import grpc
import nats
import asyncio
from .service_a_pb2 import Request, Response
from .service_a_pb2_grpc import ServiceAStub


async def consume_and_call():
    # Connect to NATS
    nc = await nats.connect("nats://nats:4222")
    js = nc.jetstream()

    # Wait for the stream to exist (created by service-b)
    print("[Service-C] Waiting for JetStream stream to be available...")
    stream_ready = False
    for i in range(60):  # Try for up to 60 seconds
        try:
            # Try to check if the stream exists directly
            try:
                stream_info = await js._jsm.stream_info("SERVICE_B_STREAM")
                if stream_info:
                    stream_ready = True
                    print(f"[Service-C] Found stream SERVICE_B_STREAM after {i+1} attempts")
                    break
            except Exception:
                # If we can't get the stream directly, check all streams
                streams = await js.streams_info()
                for s in streams:
                    if s["config"]["name"] == "SERVICE_B_STREAM" or "service-b-data" in s["config"]["subjects"]:
                        stream_ready = True
                        print(f"[Service-C] Found stream {s['config']['name']} after {i+1} attempts")
                        break
        except Exception as e:
            if i % 10 == 0:  # Log only occasionally to avoid log spam
                print(f"[Service-C] Still waiting for stream to be created... ({e})")
        await asyncio.sleep(1)
    
    if not stream_ready:
        print("[Service-C] ERROR: JetStream stream for 'service-b-data' not found after waiting.")
        return


    async def message_handler(msg):
        data = msg.data.decode()
        print(f"[Service-C] Received message: {data}")

        # Call gRPC API from service-a (optional, can be commented if not needed for test)
        async with grpc.aio.insecure_channel("service-a:50051") as channel:
            stub = ServiceAStub(channel)
            response = await stub.CallService(Request(message=data))
            print(f"Response from service-a: {response.result}")

    await js.subscribe("service-b-data", cb=message_handler)

    print("Service C is running and consuming messages from NATS JetStream (subject: service-b-data)")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(consume_and_call())
