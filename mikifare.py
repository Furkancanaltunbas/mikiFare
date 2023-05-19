import cv2
import imutils
import pyautogui

GENISLIK = 1920 
YESIL = ((29,86,6),(64,255,255))
KIRMIZI=((139,0,0),(255,160,122))
MAVI=((110,50,50),(130,255,255))
TURUNCU=((160,100,47),(179,255,255))
SARI=((10,100,100),(40,255,255))
MOR=((70,100,100),(169,255,255))

altRenk , ustRENK = MAVI

kamera = cv2.VideoCapture(0)

# betiği sonlrandırmak için kare mutlaka ekranda olmalı

cv2.namedWindow('kare')
cv2.moveWindow('kare', 10,10)
while True:
    _,kare = kamera.read()
    kare=cv2.flip(kare,1)
    
    
    kare=imutils.resize(kare,GENISLIK)
    hsv= cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    
    maske=cv2.inRange(hsv,altRenk,ustRENK)
    maske=cv2.erode(maske,None,iterations=3)
    maske=cv2.dilate(maske,None,iterations=3)    
    kopya=maske.copy()
    
    konturlar = cv2.findContours(kopya,cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(konturlar) > 0:
        kmax = max(konturlar, key=cv2.contourArea)
        (x ,y) , ycap=cv2.minEnclosingCircle(kmax)
        
        if ycap >= 20:
            #işaretciyi x y noktasına taşıyoruz.
            pyautogui.moveTo(x,y)
            cv2.circle(kare, (int(x), int(y)),
                       int(ycap), (0, 255, 255), 4)
            
   
    cv2.imshow("kare",kare)
    key=cv2.waitKey(1) & 0xFF
    
    if key == ord('q') or key == 27:
        break
    
kamera.release()
cv2.destroyAllWindows()    
    
     
            
        
    
            
    
    