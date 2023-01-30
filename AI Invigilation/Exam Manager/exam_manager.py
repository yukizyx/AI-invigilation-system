import time
class exam_manager():

    #Constant for Trigger

    # 1 : head position trigger
    # Out of boundry
    global a
    a = 1


    # 2 : head position trigger
    # Offset 30%+
    global b
    b = 2


    # 3 : Gaze Trigger
    # look around 10s +
    global c
    c = 3

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


    def set_trigger(self, constant):
        if constant == a:
            return
        elif constant == b:
            return
        elif constant == c:
            return



    def get_trigger(self):
        pass

    def start_exam(self, trigger_type, start, end, time):
        self.set_trigger(trigger_type)
        self.set_info(start, end)
        self.display_info(time)

    def end_exam(self):
        self.generate_report()

    def set_info(self, exam, new_start, new_end):
        self.exam = exam
        self.start_time = new_start
        self.end_time = new_end

    def display_info(self, in_put):
        # countdown display
        in_put = input("Input number of minutes") * 60
        self.count_down(in_put)



    # small helper function for display_info
    def count_down(self, num_of_sec):
        while num_of_sec:
            m, s = divmod(num_of_sec, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format, end='/r')
            time.sleep(1)
            num_of_sec -= 1
        print("Exam End")
