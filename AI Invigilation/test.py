import socket
import struct
import cv2
import time
import numpy as np

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8765  # The port used by the server

class SocketSender:
    def __init__(self, host, port, max_retries=10, retry_delay=1):
        self.host = host
        self.port = port
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.sock = None
        self.connect()
    
    def connect(self):
        retries = 0
        while retries < self.max_retries:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                return
            except socket.error as e:
                print(f"Failed to connect to {self.host}:{self.port}: {e}, retrying attempt {retries + 1}")
                retries += 1
                time.sleep(self.retry_delay)
        raise ConnectionError(f"Failed to connect to {self.host}:{self.port}")
    
    def send_message(self, message):
        if isinstance(message, str):
            message_type = b'STR'
            encoded_message = message.encode('utf-8')
        elif isinstance(message, np.ndarray):
            message_type = b'IMG'
            encoded_message = cv2.imencode('.jpg', message)[1].tobytes()
        else:
            raise ValueError('Invalid message type')
        message_size = struct.pack("L", len(encoded_message))
        while True:
            try:
                self.sock.sendall(message_type + message_size + encoded_message)
                break
            except socket.error as e:
                if e.errno == 10035:
                    time.sleep(0.1)
                else:
                    raise e

    def receive_message(self):
        message_type = self.sock.recv(3)
        message_size = struct.unpack("L", self.sock.recv(struct.calcsize("L")))[0]
        encoded_message = self.sock.recv(message_size)
        if message_type == b'STR':
            message = encoded_message.decode('utf-8')
        elif message_type == b'IMG':
            message = cv2.imdecode(np.frombuffer(encoded_message, np.uint8), cv2.IMREAD_COLOR)
        else:
            raise ValueError('Invalid message type')
        return message

    def close(self):
        if self.sock:
            self.sock.close()

sender = SocketSender('localhost', 8765)
sender.send_message('Hello, server!')
#use cv2 open a local image into np array
img = cv2.imread('./AI Invigilation/test.png')
sender.send_message(img)
msg = sender.receive_message()
#use cv2 to write the received image to a local file
cv2.imwrite('./AI Invigilation/test_backward.png', msg)
msg = sender.receive_message()
print(msg)