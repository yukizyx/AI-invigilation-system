

class TriggerManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TriggerManager, cls).__new__(cls)
            cls.instance.__init_default_vars()
        return cls.instance

    def __init_default_vars(self):
        self.triggers = {}
        self.triggers["mouse"] = 0.8
        self.triggers["yaw"] = 0.5
        self.triggers["pitch"] = 0.3
        return

    def set_trigger(self, trigger_name, trigger_value):
        if trigger_name in self.triggers:
            self.triggers[trigger_name] = trigger_value
        return

    def get_trigger(self, trigger_name):
        if trigger_name in self.triggers:
            return self.triggers[trigger_name]
        return None