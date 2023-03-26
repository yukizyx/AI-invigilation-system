import socket
import struct
import cv2
import time
import numpy as np
class CommunicationManager:
    def __init__(self, host, port, timeout=0):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.sock.settimeout(timeout)
        self.conn = None
        self.addr = None
    
    def accept_connection(self):
        attmp = 0
        con = False
        while not con:
            attmp += 1
            try: 
                self.conn, self.addr = self.sock.accept()
                if self.conn:
                    con = True
                    print('Connected by', self.addr)
            except socket.error as e:
                if e.errno == 10035:
                    print("No connection attemp {}, retrying after 10s ...".format(attmp))
                    time.sleep(5)
                else:
                    raise e
    
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
        self.conn.sendall(message_type + message_size + encoded_message)
    
    def receive_message(self):
        message_type = self.conn.recv(3)
        message_size = struct.unpack("L", self.conn.recv(struct.calcsize("L")))[0]
        encoded_message = self.conn.recv(message_size)
        if message_type == b'STR':
            message = encoded_message.decode('utf-8')
        elif message_type == b'IMG':
            message = cv2.imdecode(np.frombuffer(encoded_message, np.uint8), cv2.IMREAD_COLOR)
        else:
            raise ValueError('Invalid message type')
        return message
    
    def close(self):
        if self.conn:
            self.conn.close()
        self.sock.close()



