
from src import CommunicationManager
from src import utli
from src import StorageManager
from src import TriggerManager
from src.models.torch_mtcnn_custom import detect_faces
import time
import dlib
import cv2
import numpy as np
import math
from os import path

class AlgorithmControler:
    def __init__(self):
        # self.CommunicationManager = CommunicationManager.CommunicationManager()
        self.mtcnn = detect_faces
        self.landmarks = dlib.shape_predictor(path.join(".","src","models","weights","shape_predictor_68_face_landmarks.dat"))
        self.storageManager = StorageManager.StorageManager(path.join(".","test_img"))
        self.frame_number = 0
        self.triggers = TriggerManager.TriggerManager()

    def inference(self, img_in, debug_output = False):
        
        result["frame_number"] = self.frame_number
        self.frame_number = self.frame_number + 1
        bounding_boxes, landmarks = self.mtcnn(img_in)
        if len(bounding_boxes) == 0:
            result["face_detected"] = False
            return utli.pil_2_cv2(img_in), result
        else:
            result["face_detected"] = True
            gray = utli.pil_2_cv2(img_in)
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
            for face in bounding_boxes:
                face = utli.bb_2_rect(face)
                landmark = self.landmarks(gray, face)
                # Convert it to the NumPy Array
                shape_np = np.zeros((68, 2), dtype="int")
                for i in range(0, 68):
                    shape_np[i] = (landmark.part(i).x, landmark.part(i).y)
                landmark = shape_np
                #detect if mouse is open:
                avg_lip_height = (utli.dist_2d(landmark[51], landmark[62]) + utli.dist_2d(landmark[66], landmark[57]))/2
                if utli.dist_2d(landmark[62], landmark[66]) > avg_lip_height * self.triggers.get_trigger("mouse"): #TODO 0.5 is a magic number, need to be set by MI
                    result["mouse_open"] = True
                else:
                    result["mouse_open"] = False
                result["mouse_open_indicator"] = utli.dist_2d(landmark[62], landmark[66])

                #detect the yaw angle:
                left_dist = utli.dist_2d(utli.mid_point_2d(landmark[1], landmark[2]), landmark[30])
                right_dist = utli.dist_2d(utli.mid_point_2d(landmark[15], landmark[14]), landmark[30])
                result["yaw"] = (left_dist - right_dist) / max(left_dist, right_dist)
                if abs(result["yaw"]) >= self.triggers.get_trigger("yaw"):
                    result["yaw_violated"] = True
                else:
                    result["yaw_violated"] = False

                #detect the pitch angle:
                # face_height = utli.dist_2d(utli.mid_point_2d(landmark[21], landmark[22]), landmark[8])
                # face_width = utli.dist_2d(landmark[0], landmark[16])
                # result["pitch"] = face_width / face_height
                face_width_mid = utli.mid_point_2d(utli.mid_point_2d(landmark[1], landmark[2]), utli.mid_point_2d(landmark[15], landmark[14]))
                face_mid_to_nose = utli.dist_2d(face_width_mid, landmark[30])
                face_distance_to_mid_half = (left_dist + right_dist)/2
                result["pitch"] = face_mid_to_nose / face_distance_to_mid_half
                print("pitch: " + str(result["pitch"]))
                if result["pitch"] >= self.triggers.get_trigger("pitch"):
                    result["pitch_violated"] = True
                else:
                    result["pitch_violated"] = False

        if debug_output == True:
            img_cv2 = utli.pil_2_cv2(img_in)
            #draw landmark
            for i, (x, y) in enumerate(landmark):
                cv2.circle(img_cv2, (x, y), 1, (0, 0, 255), -1)

            #draw mouth open line
            if result["mouse_open"] == True:
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)
            cv2.line(img_cv2, (landmark[62][0], landmark[62][1]), (landmark[66][0], landmark[66][1]), color, thickness=1)

            #draw yaw line
            if result["yaw_violated"] == True:
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)
            cv2.line(img_cv2, utli.mid_point_2d(landmark[1], landmark[2], to_int=True), landmark[30], color, thickness=1)
            cv2.line(img_cv2, utli.mid_point_2d(landmark[15], landmark[14], to_int=True), landmark[30], color, thickness=1)

            #draw pitch line
            if result["pitch_violated"] == True:
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)

            cv2.line(img_cv2, utli.mid_point_2d(landmark[21], landmark[22], to_int=True), landmark[8], color, thickness=1)

            if self.frame_number % 10 == 0:
                self.storageManager.saveFrame(img_cv2, "test" + str(self.frame_number) + ".jpg")
            return img_cv2, result

        self.storageManager.saveFrame(img_cv2, "test" + str(self.frame_number) + ".jpg")
        return utli.pil_2_cv2(img_in), result