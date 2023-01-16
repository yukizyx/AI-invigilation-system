import random
class system:
    def __init__(self, user_type, exam_manager):
        self.user_type = user_type


    def generate_supervisor(self):
        global pass_supervisor
        pass_supervisor = hash(random.random)

    def generate_staff(self):
        global pass_staff
        pass_staff = hash(random.random)


    def authenticate_supervisor(self, hashcode):
        if hashcode == pass_supervisor:
            return True
        else:
            return False


    def authenticate_staff(self, hashcode):
        if hashcode == pass_staff:
            return True
        else:
            return False

