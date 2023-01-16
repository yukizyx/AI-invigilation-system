class exam_manager:
    def __init__(self, exam, dm, vc, state, start_time, end_time):
        self.exam = exam
        self.state = state
        self.start_time = start_time
        self.end_time = end_time

    def generate_report(self):
        with open('report.txt', 'w') as f:
            f.write(self.exam)
            f.write(self.start_time)
            f.write(self.end_time)


    def set_trigger():
        pass


    def get_trigger():
        pass

    def start_exam():
        pass

    def end_exam():
        pass

    def set_info(self, new_start, new_end):
        self.start_time = new_start
        self.end_time = new_end

    def display_info():
        pass


