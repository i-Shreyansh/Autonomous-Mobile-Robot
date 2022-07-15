import time
import numpy as np
import  pandas as pd
import os
import cv2
from  PIL import Image

def loader():
    cmd("cls")
    for i in range(5):
        time.sleep(0.5)
        print('.',end='')
    print("done")



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

def read_file(file):
    file = open(file,'r')
    file = file.read()
    return file
def write_file(file,data) :
    loader()
    with open(file,'w') as f:
        f.write(str(data))
    



