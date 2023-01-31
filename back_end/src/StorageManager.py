import os
import cv2

class StorageManager:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        #create now dir if not exists
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
            print("Created storage directory: " + self.storage_path)
        return

    def saveFrame(self, frame, file_name):
        cv2.imwrite(self.storage_path + "/" + file_name, frame)