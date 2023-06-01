import subprocess
import sys
import time


def main():
    # Launch the server
    server = subprocess.Popen([sys.executable, 'server.py'])

    # Give the server time to start up before we launch the client
    time.sleep(2)

    # Launch the client
    client = subprocess.Popen([sys.executable, 'client.py'])

    # We don't use communicate() here because that would block the main script until the server and client finish running
    # We just start the server and client and let them run

    try:
        server.wait()
        client.wait()
    except KeyboardInterrupt:
        # Terminate the server and client when Ctrl+C is pressed
        server.terminate()
        client.terminate()


if __name__ == '__main__':
    main()
