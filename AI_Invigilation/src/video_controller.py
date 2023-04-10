from src.exam_manager import * 
from src.camera_controler import *

import cv2
import numpy as np
import threading

def get_avaiable_cam_count():
    count = 0
    while True:
        cap = cv2.VideoCapture(count)
        if cap is None or not cap.isOpened():
            break
        else:
            count += 1
        cap.release()
    return count


class video_controller:
    global new_exam
    new_exam = exam_manager

    def __init__(self, report, path):
        self.report = report
        self.path = path
        self.cap = []
        self.thread = []
        self.count = 0
        self.status = False

    def init_camera(self, config):
        count = get_avaiable_cam_count()
        #read config file black_list
        black_list = config['Camera']['black_list']
        black_list = black_list.split(',')
        black_list = [int(i) for i in black_list]

        for i in range(count):
            if i in black_list:
                count -= 1
                continue
            cam = camera_controler(i,self.path)
            self.cap.append(cam)
        self.status = True


    def release_camera(self):
        for cam in caps:
            cam.release_camera()
        for thread in self.thread:
            thread.join()
        self.status = False

    def start_Recording(self):
        if self.status == False:
            self.init_camera()
        for cam in self.cap:
            thread = threading.Thread(target=recording_thread, args=(cam,))
            thread.start()
            self.thread.append(thread)

    def end_Recording(self):
        for cam in self.cap:
            cam.stop_recording()


    def get_next_detection_frame(self):
        frame = None
        while frame is None:
            cam = self.cap[self.count]
            frame = cam.get_current_frame()
            self.count = (self.count + 1) % len(self.cap)
            return frame

