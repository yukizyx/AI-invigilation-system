import cv2
import os
class storage_manager:
    def __init__(self, report_path, file_name):
        self.report_path = report_path
        self.report = []
        self.file_name = file_name
        self.count = 0
    
    def add_report(self, report):
        self.count += 1
        self.report.append(report)
        if self.count % 10 == 0:
            self.save_report()

    def save_report(self):
        #check if report folder exist
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)
        #check if report file exist
        if not os.path.exists(self.report_path + '/' + self.file_name):
            with open(self.report_path + '/' + self.file_name, 'w') as file:
                file.write('')
        #write report to file
        with open(self.report_path + '/' + self.file_name, 'a') as file:
            for report in self.report:
                file.write(str(report))

    def save_image(self, img, frame_id):
        cv2.imwrite(self.report_path + '/' + str(frame_id) + '.jpg', img)