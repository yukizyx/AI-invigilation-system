import socket
import struct
import cv2
import time
import numpy as np
import json
from src.image_manager import *
from src.storage_manager import *
from src.trigger import *

class connection_manager:
    def __init__(self, host, port, max_retries=10, retry_delay=1):
        self.host = host
        self.port = port
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.sock = None
        self.sending = False
        self.storage_manager = storage_manager('report', 'report.txt')
        self.imageManager = image_manager()
        self.tm = trigger()

    def connect(self):
        retries = 0
        while retries < self.max_retries:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                self.sock.setblocking(False)
                return True
            except socket.error as e:
                print(f"Failed to connect to {self.host}:{self.port}: {e}, retrying attempt {retries + 1}")
                retries += 1
                time.sleep(self.retry_delay)
        return False
        # raise ConnectionError(f"Failed to connect to {self.host}:{self.port}")

    def start_sending(self, video_controller):
        self.sending = True
        while self.sending:
            idx, frame = video_controller.get_next_detection_frame()
            if frame is None:
                continue
            self.send_message(frame)
            frame = self.receive_message()
            if frame is not None:
                self.imageManager.save_image(idx, frame)
            # cv2.imshow('frame', res)
            # cv2.imwrite('test.jpg', res)
            res = self.receive_message()
            tri = self.tm.get_trigger()
            if res is not None:
                #save 
                res = json.loads(res)
                if res['face_detected']:
                    if (res['mouse_open'] and tri[0]) or (res['yaw_violated'] and tri[1]) or (res['pitch_violated'] and tri[2]):
                        print("Detected on cam{}".format(idx))
                        self.storage_manager.add_report(res)
                        self.storage_manager.save_image(frame, res['frame_number'])
            time.sleep(0.1)
    
    def end_sending(self):
        self.sending = False

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
        while True:
            try:
                message_type = self.sock.recv(3)
            except Exception as e:
                pass
            else:
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