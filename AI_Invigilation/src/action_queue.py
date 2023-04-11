import threading
from functools import wraps
from collections import deque
from src.image_manager import singleton

SET_TRIGER = 0
SET_CAMERA = 1
START_EXAM = 2

@singleton
class ActionQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def add_action(self, action, value):
        with self.lock:
            self.queue.append((action, value))

    def get_top_action(self):
        with self.lock:
            if not self.queue:
                return None
            return self.queue[0]

    def remove_action(self):
        with self.lock:
            if not self.queue:
                return None
            return self.queue.popleft()

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0