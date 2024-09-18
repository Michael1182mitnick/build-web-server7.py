# Asynchronous_Web_Server_Using_asyncio
# Use Python's asyncio library to create an asynchronous web server that can handle multiple client connections concurrently.

import asyncio

# Handle a single client connection


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected by {addr}")

    while True:
        # Read the data from the client
        data = await reader.read(100)
        message = data.decode()
        if not message:
            break  # Client disconnected

        print(f"Received {message} from {addr}")

        # Send response back to the client
        writer.write(data)
        await writer.drain()  # Ensure the data is sent before proceeding

    print(f"Connection closed by {addr}")
    writer.close()  # Close the writer (connection)
    await writer.wait_closed()

# Main function to run the server


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()  # Keep the server running

# Run the asyncio event loop
asyncio.run(main())
