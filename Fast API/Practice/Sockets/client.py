import socketio
import asyncio

sio_client = socketio.AsyncClient()

@sio_client.event
async def connect():
    print(f"I'm Connected")

@sio_client.event
async def disconnect():
    print(f"I'm Disconnted")

async def main():
    await sio_client.connect(url='http://localhost:8000', socketio_path="sockets")
    await sio_client.disconnect()

asyncio.run(main())