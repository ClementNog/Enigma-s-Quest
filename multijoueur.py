import socket
import threading

class Jeu:

    def __init__(self):
        self.serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip, self.port = '127.0.0.1', '9999'
        self.client_socket, self.address = None, None
        self.serveur.bind((self.ip, self.port))
        self.serveur.listen(1)

    def attendre_connexion(self):

        self.client_socket, self.address = self.serveur.accept(b) 