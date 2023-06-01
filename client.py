import asyncio
import json
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            variables = json.loads(data)
            print(f"A: {variables['A']}, B: {variables['B']}, C: {variables['C']}")

asyncio.get_event_loop().run_until_complete(client())
