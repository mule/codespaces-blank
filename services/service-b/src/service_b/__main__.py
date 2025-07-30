

import asyncio
import nats
import time
import signal
import sys
import os

# Signal handler to gracefully exit on SIGTERM/SIGINT
def signal_handler(sig, frame):
    print("Shutting down service-b...")
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

async def setup_nats():
    # Connect to NATS
    nc = await nats.connect("nats://nats:4222")
    js = nc.jetstream()
    
    # Add a stream if it doesn't exist
    try:
        await js.add_stream(name="SERVICE_B_STREAM", subjects=["service-b-data"])
        print("Stream SERVICE_B_STREAM created successfully")
    except Exception as e:
        if "already in use" not in str(e):
            print(f"Error adding stream: {e}")
        else:
            print("Stream SERVICE_B_STREAM already exists")
    
    return nc, js

async def produce_messages():
    nc, js = await setup_nats()
    
    # Send a few test messages
    for i in range(3):
        msg = f"Test message {i+1} from service-b"
        await js.publish("service-b-data", msg.encode())
        print(f"Published: {msg}")
    
    # Keep the connection open
    print("Service-B is running and ready to serve")
    
    # Create health check file to indicate readiness
    with open("/tmp/healthy", "w") as f:
        f.write("ready")
    
    # Keep the service running
    while True:
        await asyncio.sleep(10)
        # Optionally publish more messages periodically
        msg = f"Periodic message at {time.time()}"
        await js.publish("service-b-data", msg.encode())
        print(f"Published periodic message: {msg}")

if __name__ == "__main__":
    try:
        asyncio.run(produce_messages())
    except KeyboardInterrupt:
        print("Service stopped by user")
    except Exception as e:
        print(f"Error in service-b: {e}")
        sys.exit(1)
