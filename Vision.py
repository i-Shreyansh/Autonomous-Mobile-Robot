from unittest import result
from PIL import Image
import cv2
from cv2 import waitKey
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

def stackImages(scale,imgArray,border=False):
    if border==True:
        h,v=imgArray
        for i in range(len(h)):
            h[i] = Border(h[i])
        for i in range(len(v)):
            v[i] = Border(v[i])
        imgArray = (h,v)

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

def colors():
    col = {'red':(36,51,235),'green':(77,249,117),"blue":(245,35,0),
            'yellow':(85,253,255),'black':(0,0,0,),'white':(255,255,255),
            'pink':(128,54,234),'orange':(80,134,240),'violet':(123,16,57),
            'purple':(124,27,116),'brown':(21,67,120),'sky blue':(253,251,115),
            'olive':(38,127,129),'gray':(192,192,192),'teal':(128,127,80),
            'dark green':(12,62,24),'skin':(130,158,240),'lavender':(187,130127)}
    return col

def Rectangle(img,x,y,h,w,color=(0,0,255),thick=2,fill=False):
    if fill== True:
        var = cv2.FILLED
    else:
        var = thick
    img = cv2.rectangle(img,(x,y),(x+w,y+h),color,var)
    return img
def Border(image,top=10,bottom=10,left=10,right=10,
         type=cv2.BORDER_CONSTANT, color=0):

    img = cv2.copyMakeBorder(image, top, bottom, left, right,
                             type, None, value = color)
    return img

def ScrollBar():
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars",640,250)
    cv2.createTrackbar("Hue Min","TrackBars",0,179,lambda a: a)
    cv2.createTrackbar("Hue Max","TrackBars",179,179,lambda a: a)
    cv2.createTrackbar("Sat Min","TrackBars",0,255,lambda a: a)
    cv2.createTrackbar("Sat Max","TrackBars",255,255,lambda a: a)
    cv2.createTrackbar("Val Min","TrackBars",0,255,lambda a: a)
    window = cv2.createTrackbar("Val Max","TrackBars",0,255,lambda a: a)
    return window
def Values():   
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    return h_min,h_max,s_min,s_max,v_min,v_max
def Mask(img):

    h_min,h_max,s_min,s_max,v_min,v_max = Values()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    return mask

camera(1)
if __name__ == '__main__':
    #loader()
    cmd('cls')
    photo = "img.jpg"
    global col
    col = colors()
    ScrollBar()

    while True:
        img = cv2.imread(photo)
        img = imgResize(img,500,500)
        print(Values())
        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask = Mask(img)
        imgResult = cv2.bitwise_and(img,img,mask=mask)     

                
        result = stackImages(0.6,([img,imgHSV],[mask,imgResult]),True)
        cv2.imshow("images" , result)

        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
    


