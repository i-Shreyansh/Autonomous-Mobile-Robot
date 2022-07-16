
from cv2 import rectangle
from Libraries import *
from Train import *
from Vision import *
import json



def run():
    loader()

if __name__ == '__main__':
  
    run()
    col = colors()
    keys = pd.read_csv("credentials.csv")
    access_key,secret_key = keys['Access key ID'].values[0],keys['Secret access key'].values[0]
    AWS_keys(access_key,secret_key)

    #photo location
    photo = input("Enter image path : ")
    maxLabels = int(input("Max no. of labels : "))


    response = aws_detect_labels(photo,20)
    write_file('res.txt',response)
    response = str(read_file('res.txt'))

    re = str(response)
    re = re.replace("\'", "\"")
   
    re = json.loads(re)
    
    
    while  True:

        img = cv2.imread(photo)
        rect = img.copy()
        H,W=rect.shape[0], rect.shape[1]

        for labels in re['Labels']:
            x,y,w,z=0,0,0,0
            print(labels["Name"])
            for inst in labels["Instances"]:
                x = float(inst["BoundingBox"]['Left'])*W
                y = float(inst["BoundingBox"]['Top'])*H
                w = float(inst["BoundingBox"]['Width'])*W
                h = float(inst["BoundingBox"]['Height'])*H
                
   
                x,y,w,h = int(x),int(y),int(w),int(h)
                print(x,y,w,h)     
                rect = Rectangle(rect,x,y,w,h,col['red'],10)
                rect = Text(rect,labels['Name'],(x,y),5,col['blue'],18)
      
        

        imgStack = stackImages(0.5,([img,rect]))
        cv2.imshow("Stack", imgStack)
      
        
        if cv2.waitKey(1) &  0xFF == 27:
            break
   
    cv2.destroyAllWindows()

