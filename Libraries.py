import cv2
import time
from PIL import Image
import numpy as np
import  pandas as pd
import os

def loader():
    for i in range(5):
        time.sleep(1)
        print('.',end='')
    print("done")

def camera(device=0):
    global cam
    cam = device
    return cam

def Showcam():
    vid = cv2.VideoCapture(cam)
    
  
    while(True):
        global frame
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
        
    vid.release()
    cv2.destroyAllWindows()

def cv2_to_pil(frame):
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(im)
    im.show()  
    im_np = np.asarray(im) 
    return im_np

def pil_to_cv2(PILframe):
    im = cv2.cvtColor(PILframe, cv2.COLOR_RGB2BGR)
    cv2.imshow("Frame",im)
    cv2.waitKey(5000)

    return im

def cmd(command):
    str='cmd /c "%s"'%(command)
    os.system(str)

def read_file(Name):
    file = open(Name,'r')
    file = file.read()
    return file


camera(0)

if __name__ == '__main__':
    #loader()
    camera(0)
    Showcam()



    