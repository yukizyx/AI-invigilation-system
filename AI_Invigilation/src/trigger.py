from src.image_manager import singleton

@singleton
class trigger:
    def __init__(self):
        self.trigger = [True] * 3

    def get_trigger(self):
        return self.trigger


    def set_trigger(self, trigger):
        self.trigger = trigger
        
