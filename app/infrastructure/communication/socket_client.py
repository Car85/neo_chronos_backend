from socketIO_client_nexus import SocketIO

class SocketClient:
    def __init__(self, host="localhost", port=8000, transports=["xhr-polling"]):
        self.socketIO = SocketIO(host, port, transports=transports)

    def send(self, message):
        self.socketIO.emit("backend", message)
        self.socketIO.wait(seconds=1)
