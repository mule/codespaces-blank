
import asyncio
import nats
from flask import Flask

app = Flask(__name__)

async def setup_nats_and_send():
    nc = await nats.connect("nats://nats:4222")
    js = nc.jetstream()
    # Add a stream if it doesn't exist
    try:
        await js.add_stream(name="SERVICE_B_STREAM", subjects=["service-b-data"])
    except Exception as e:
        if "already in use" not in str(e):
            print(f"Error adding stream: {e}")
    # Send a few test messages
    for i in range(3):
        msg = f"Test message {i+1} from service-b"
        await js.publish("service-b-data", msg.encode())
        print(f"Published: {msg}")
    await nc.close()

@app.before_first_request
def start_nats():
    loop = asyncio.get_event_loop()
    loop.create_task(setup_nats_and_send())

@app.route("/")
def home():
    return "Service B is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
