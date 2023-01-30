class trigger:

    global head_position_trigger
    head_position_trigger = False
    global gaze_trigger
    gaze_trigger= False

    def __init__(self, description, duration, state):
        self.description = description
        self.duration = duration
        self.state = state
    def active_trigger(self, name):
        if name == "head_position_trigger":
            head_position_trigger = True
        if name == "gaze_trigger":
            gaze_trigger = True


    def cancel_trigger(self, name):
        if name == "head_position_trigger":
            head_position_trigger = False
        if name == "gaze_trigger":
            gaze_trigger = False


    def set_trigger(self):
        pass
