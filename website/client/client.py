from socket import AF_INET, socket, SOCK_STREAM 
from threading import Thread, Lock
import time

class Client:

    HOST = "localhost"
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFSIZ = 512

    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()

    def receive_messages(self):
    # получаем сообщения от серера
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()

                # безопасный доступ к памяти
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[ОШИБКА]", e)
                break 

    def send_message(self, msg):
        # отправляем сообщения серверу
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()

    def get_messages(self):
        messages_copy = self.messages[:]

        # безопасный доступ к памяти
        self.lock.acquire()
        self.messages = []
        self.lock.release()

        return messages_copy

    def disconnect(self):
        self.send_message("{вышел}")