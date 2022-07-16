
import re
from unittest import result
from PIL import Image
import cv2
from cv2 import waitKey
from cv2 import bitwise_and
from pyparsing import col
from Libraries import * 

def camera(device=0):
    global cam
    cam = device
    return cam


        
    vid.release()
    
def Showcam():
    vid = cv2.VideoCapture(cam)
    
  
    while(True):
        global frame
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) &  0xFF == ord('q'):
            break

def imgResize(img,width,height):
    imgResize = cv2.resize(img,(width,height))
    return imgResize

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def joinImages(ImgArr,horizontal=True,border=False):
    if border==True:
        ImgArr = list(ImgArr)
        for i in range(len(ImgArr)):
            ImgArr[i] = Border(ImgArr[i])
        ImgArr = tuple(ImgArr)

    if horizontal == True:
        img = np.hstack(ImgArr)
    else:
        img = np.vstack(ImgArr)
        
    return img

def colors(mode='bgr'):
    global col
    col = {'red':(36,51,235),'green':(77,249,117),"blue":(245,35,0),
            'yellow':(85,253,255),'black':(0,0,0,),'white':(255,255,255),
            'pink':(128,54,234),'orange':(80,134,240),'violet':(123,16,57),
            'purple':(124,27,116),'brown':(21,67,120),'sky blue':(253,251,115),
            'olive':(38,127,129),'gray':(192,192,192),'teal':(128,127,80),
            'dark green':(12,62,24),'skin':(130,158,240),'lavender':(187,130,127)}
    if mode == 'bgr':
        return col
    elif mode == 'rgb':
        for i in col.items():
            color,tuple = i
            b,g,r = tuple
            tuple = (r,g,b)
            col[color] = tuple
        

        return col

def Rectangle(img,x,y,w,h,color=(0,0,255),thick=2,fill=False):
    if fill== True:
        var = cv2.FILLED
    else:
        var = thick
    x,y,w,h = int(x),int(y),int(w),int(h)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),color,var)
    return img

def  Text(img,txt,pt,scale,color,thick):
    img = cv2.putText(img,txt,pt,cv2.FONT_HERSHEY_COMPLEX,scale,color,thick)
    return img

def Border(image,top=10,bottom=10,left=10,right=10,
         type=cv2.BORDER_CONSTANT, color=0):

    img = cv2.copyMakeBorder(image, top, bottom, left, right,
                             type, None, value = color)
    return img

#COLOR DETECTION :
def ScrollBar():
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,250)
    cv2.createTrackbar("Hue Min","TrackBars",0,1790,lambda a: a)
    cv2.createTrackbar("Hue Max","TrackBars",1790,1790,lambda a: a)
    cv2.createTrackbar("Sat Min","TrackBars",0,2550,lambda a: a)
    cv2.createTrackbar("Sat Max","TrackBars",2550,2550,lambda a: a)
    cv2.createTrackbar("Val Min","TrackBars",0,2550,lambda a: a)
    window = cv2.createTrackbar("Val Max","TrackBars",0,2550,lambda a: a)
    return window
def Values():   
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")/10
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")/10
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")/10
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")/10
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")/10
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")/10
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    return h_min,h_max,s_min,s_max,v_min,v_max
def Mask(img,HSV_arr):

    h_min,h_max,s_min,s_max,v_min,v_max = HSV_arr
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    return mask

def BITWISE_and(img,mask):
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    return imgResult

#Shape detection:
 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    return contours

def drawCountours(contours,imgContour):
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area<500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
def addImages(img1,w1,img2,w2):
    img = cv2.addWeighted(img1, w1, img2, w2, 0.0);
    return img

#FaceDetection
def face_detection(img,color):
    facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = facecascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
            face = Rectangle(img,x,y,w,h,color)
    #cv2.imshow("Face_Detection",img)
    return  img


