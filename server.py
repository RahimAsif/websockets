import asyncio
import random
import json
import websockets


async def server(websocket, path):
    while True:
        # Randomly generating variables A, B and C
        A = random.randint(0, 100)
        B = random.randint(0, 100)
        C = random.randint(0, 100)

        # Packing the variables into a dictionary and converting it to JSON
        data = json.dumps({'A': A, 'B': B, 'C': C})

        # Sending the data to the client
        await websocket.send(data)

        # Waiting for 1 second before sending the next set of variables
        await asyncio.sleep(0.25)

start_server = websockets.serve(server, 'localhost', 8765)

print("Starting server...")
asyncio.get_event_loop().run_until_complete(start_server)
print("Server is running!")
asyncio.get_event_loop().run_forever()
