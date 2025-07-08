from server.main import Server
from config import HOST, PORT

if __name__ == "__main__":
    server = Server(host=HOST, port=PORT)

    server.start()