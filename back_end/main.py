import cv2
import argparse
import time

from PIL import Image
from src import utli
from src import AlgorithmControler
from src import TriggerManager

FPS = 30

def get_args():
    opt = argparse.ArgumentParser()
    opt.add_argument('--local', type=bool, default = True, help='run on local machine')
    opt.add_argument('--backup_dir', type=str, default='./backup', help='frame backup dir')
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
        print("Online mode, awaiting for income frame ...")

        #TODO next deliverbale do this part
        img = cv2.imread('./test_img/test.jpg')
        img = utli.cv2_2_pil(img)
        #detect face
        ac.inference(img, debug_output=True)
