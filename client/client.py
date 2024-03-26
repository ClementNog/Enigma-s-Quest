import socket
import threading
import json
from protocols import Protocols


class Client:
    def __init__(self, host="127.0.0.1", port=55555):
        self.nickname = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))
        self.map = self.get_map()
        self.wall_positions = self.get_map()
        self.closed = False
        self.started = False
        self.text= False
        self.opponent_data = None
        self.winner = None

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
    
    def get_map(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.map()

    def get_wall(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.wall()

    def send(self, request, message):
        data = {"type": request, "data": message}
        self.server.send(json.dumps(data).encode("ascii"))

    def receive(self):
        while not self.closed:
            try:
                data = self.server.recv(1024).decode("ascii")
                message = json.loads(data)
                self.handle_response(message)
            except:
                break
        
        self.close()

    def close(self):
        self.closed = True
        self.server.close()

    def handle_response(self, response):
        r_type = response.get("type")
        data = response.get("data")
        
        if r_type == Protocols.Response.MAP:
            self.map = data
        elif r_type == Protocols.Response.OPPONENT:
            self.opponent_data = data
        elif r_type == Protocols.Response.START:
            self.started = True
        elif r_type == Protocols.Response.WALL:
            self.wall_positions = data
        elif r_type == Protocols.Response.CAN:
            self.text = data

