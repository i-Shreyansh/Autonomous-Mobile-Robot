import pygame
from Vision import *
from Libraries import *

def cv2img_to_pygame(cv2img):
    """Convert cvimage into a pygame image"""
    img_rgb = cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
    img_rgb = np.rot90(img_rgb)
    frame = pygame.surfarray.make_surface(img_rgb).convert()
    frame = pygame.transform.flip(frame,False,False)
    return frame
def TextPygame(txt,size=100,color=(0,0,0)):
    font = pygame.font.Font(None,size)
    text = font.render(txt,False,color)
if __name__ == '__main__':
    cmd('cls')
    col = colors('rgb')
    pygame.init()  
   
    # assigning values to height and width variable   
    width = 1000
    height = 480
    # creating the display surface object   
    # of specific dimension..e(X, Y).   
    display_surface = pygame.display.set_mode((width, height))  
    
    # set the pygame window name   
    pygame.display.set_caption('Image')  
    
    vid =cv2.VideoCapture(0)

    fps = 60 
    cloack = pygame.time.Clock()
    
    # infinite loop 
    start = True  
    while start:  
        success , frame = vid.read()
        frame = imgResize(frame,720,470)
        frame = face_detection(frame,col['blue'])
        #cv2.imshow('frame', frame)
        image = cv2img_to_pygame(frame)
        image2 = pygame.image.load('Download.png')

        display_surface.fill(col['white'])  
        display_surface.blit(image, (10,0))  
        display_surface.blit(image2, (650,380))  

        pygame.display.update() 
        cloack.tick(fps)  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                start = False  
                pygame.quit() 
        
                
                # quit the program.   
        # Draws the surface object to the screen.   
    vid.release()
    cv2.destroyAllWindows()