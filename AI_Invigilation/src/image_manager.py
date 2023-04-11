import cv2
import threading
from functools import wraps

def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class image_manager:
    def __init__(self):
        self.images = {}
        self.lock = threading.Lock()

    def save_image(self, filename, img):
        with self.lock:
            self.images[filename] = img

    def read_image(self, filename):
        with self.lock:
            if filename in self.images:
                return self.images[filename]
            else:
                return None

