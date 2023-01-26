from student import student
class Message(student):
    def __init__(self, student, timestamp, trigger, display, dismiss):
        self.student = student
        self.timestamp = timestamp
        self.trigger = trigger
        self.display = display
        self.dismiss = dismiss


    def show_message(self):
        pass


    def hide_message(self):
        pass


    def dismiss_message(self):
        pass
