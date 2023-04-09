from exam_manager import *
class video_controller:
    global new_exam
    new_exam = exam_manager

    def __init__(self, report, path):
        self.report = report
        self.path = path

    def start_Recording(self, date):
        #first take several inputs from the prompt
        trigger_type = input("please enter the trigger type")
        start = input("please enter the start time of the exam")
        end = input("please enter the end time of the exam")
        time = input("please enter duration of the exam")

        #functions are all completed configured in the exam_manager(start_exam)
        new_exam.start_exam(trigger_type, start, end, time)

    def end_Recording(self):
        new_exam.end_exam()


    def send_Next_detection_frame(self, file):
        pass
        

