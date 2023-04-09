import cv2
import datetime
import threading

class camera_controler:
    def __init__(self, index, path, video_duration=60):
        self.index = index
        self.cap = cv2.VideoCapture(index)
        self.path = path
        self.video_duration = video_duration
        self.cap = cv2.VideoCapture(self.index)
        self.current_frame = None
        self.recording = False
        self.lock = threading.Lock()
    
    def start_recording(self):
        self.recording = True
        while self.recording:
            start_time = datetime.datetime.now()
            filename = f'{self.path}/video_{self.index}_{start_time.strftime("%Y%m%d_%H%M%S")}.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = int(self.cap.get(cv2.CAP_PROP_FPS))
            frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            out = cv2.VideoWriter(filename, fourcc, fps, frame_size)

            while (datetime.datetime.now() - start_time).seconds < self.video_duration:
                ret, frame = self.cap.read()
                if ret:
                    with self.lock:
                        self.current_frame = frame.copy()
                    out.write(frame)

            out.release()
        self.cap.release()

    def get_current_frame(self):
        with self.lock:
            return self.current_frame.copy()

    def stop_recording(self):
        self.recording = False
        
    def release_camera(self):
        self.cap.release()

def recording_thread(camera_recorder):
    camera_recorder.start_recording()

