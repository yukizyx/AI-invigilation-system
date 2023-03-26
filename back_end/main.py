import cv2
import argparse
import time
import socket
import threading
import numpy as np

from PIL import Image
from src import utli
from src import AlgorithmControler
from src import TriggerManager
from src import CommunicationManager

FPS = 30

def get_args():
    opt = argparse.ArgumentParser()
    opt.add_argument('--local', type=bool, default = False, help='run on local machine')
    opt.add_argument('--backup_dir', type=str, default='./backup', help='frame backup dir')
    opt.add_argument('--port', type=int, default=8765, help='port for socket')
    opt.add_argument('--ip', type=str, default='127.0.0.1', help='ip for socket')

    args = opt.parse_args()
    return args

def gen_hash():
    import random
    hash_supervisor = random.getrandbits(128)
    hash_invigilator = random.getrandbits(128)
    return hex(hash_supervisor), hex(hash_invigilator)

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

if __name__ == "__main__":
    args = get_args()
    ac = AlgorithmControler.AlgorithmControler()
    triggers = TriggerManager.TriggerManager()
    print("System Initiated ...")
    hash_s, hash_i = gen_hash()
    print("Supervisor hash: " + hash_s)
    print("Invigilator hash: " + hash_i)
    #save both hash to file
    with open('./hash.txt', 'w') as f:
        f.write("supervisor:" + hash_s + '\n' + "invigilator:" + hash_i)
    print("Hash saved to ./hash.txt")

    #cv2 load image
    if args.local :
        count = get_avaiable_cam_count()
        print("Local mode, {} cams detected, starting captures ...".format(count))
        print("Press 'q' to quit")
        caps = []


        for i in range(count):
            caps.append(cv2.VideoCapture(i))

        while True:
            if cv2.waitKey(int(1/FPS*1000)) & 0xFF == ord('q'):
                break
            for i in [0]: #TODO FIX THIS
                cam = caps[i]
                ret, img = cam.read()
                img = utli.cv2_2_pil(img)
                #detect face
                #time the function
                img, res = ac.inference(img, debug_output=True)
                cv2.imshow('cam:{}'.format(i), img)

        for cam in caps:
            cam.release()
        cv2.destroyAllWindows()

    else :
        #online mode
        print("Online mode, start listining on port {} ...".format(args.port))
        cm = CommunicationManager.CommunicationManager(args.ip, args.port)
        cm.accept_connection()
        while True:
            if cv2.waitKey(int(1/FPS*1000)) & 0xFF == ord('q'):
                break
            try:
                res = cm.receive_message()
                if isinstance(res, str):
                    #todo do shit here
                    print("Received message: " + res)
                elif isinstance(res, np.ndarray):
                    img = utli.cv2_2_pil(res)
                    #detect face
                    img, res = ac.inference(img, debug_output=True)
                    cm.send_message(img)
                    cm.send_message(str(res))
            except socket.timeout:
                print('Timed out waiting for connection')
                cm.close()
                exit(0)


        # #TODO next deliverbale do this part
        # img = cv2.imread('./test_img/test.jpg')
        # img = utli.cv2_2_pil(img)
        # #detect face
        # ac.inference(img, debug_output=True)
