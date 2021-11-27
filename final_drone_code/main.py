from utils import *
import time
import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
cnt = 0
lr_state=0
ud_state=0
fs_state=0
stable_state = 1
phase = 0
movefb = 0

def move_drone(myDrone,phase):
    arr = phase % 4
    mnt = phase // 4
    if arr == 0:
        myDrone.move_up((1+mnt)*20)
        time.sleep(1)
    elif arr == 1:
        myDrone.move_left((1+mnt)*20)
        time.sleep(1)
    elif arr == 2:
        myDrone.move_down((1+mnt)*20)
        time.sleep(1)
    elif arr == 3:
        myDrone.move_right((1+mnt)*20)
        time.sleep(1)    
    return 0

if __name__ == "__main__":
    myDrone = initTello()    
    myDrone.streamon() 
    time.sleep(1)  
    frame_read = myDrone.get_frame_read()
    time.sleep(1)
    myDrone.takeoff()
    time.sleep(1)

    while True:
        img = frame_read.frame
       
        # Change to grayscale
        frame_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces first
        faces = face_detector.detectMultiScale(frame_grayscale)       
        
            
        # Run face detector within each of those faces
        for (x, y, w, h) in faces:

            # Check the size of faces
            print("size is {}".format(w*h))

            # Draw a rectangle around the face
            cv2.rectangle(img, (x,y), (x+w, y+h), (100, 200, 50), 4)
        
            # Get the sub frame (using numpy)
            the_face = img[y:y+h, x:x+w]    

            # Change to gray Scale
            face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

            # Run smile Detector on sub frame with some factors (to recognize more accurate)
            smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
            # Check the smile(screenshot)
            if len(smiles) > 0 and stable_state == 1:
                print("it smile!")
                cv2.imwrite('screenshot{}.png'.format(cnt), img) # Save Screen shot with cv method
                cnt += 1
        
        # Show the current frame
        cv2.imshow("drone",img)

        # Keep update the frame and wait for keyboard input
        keyboard = cv2.waitKey(1)

        # System shut down key 'q'
        if keyboard & 0xFF == ord('q'):
            print("system shut down")
            myDrone.land()
            time.sleep(1)
            frame_read.stop()
            time.sleep(1)
            myDrone.streamoff()
            time.sleep(1)

        # Check the faces wether there is no faces at firts, move around until find faces
        # Drone can't found face yet
        if len(faces) == 0:
            print("no face!")
            print("face find algorithm start.")           
            move_drone(myDrone,phase)
            phase += 1

        # Drone found only one face
        elif len(faces) == 1:
            phase = 0
            print("face!")
            #scale the balance of left and right and move the drone        
            xrt = faces[0][0] / 600-(faces[0][0]+faces[0][2])
            if xrt > 1.2:
                lr_state=0
                print("too left")
                myDrone.move_left(20)
                 
                time.sleep(1)                
            elif xrt < 0.7:
                lr_state=0
                print("too right")
                myDrone.move_right(20) 
                              
                time.sleep(1)                
            else:
                print("leftright stable")
                lrstate = 1

            #scale the balance of high and low and move the drone
            yrt = faces[0][1] / 400-(faces[0][1]+faces[0][3])
            if yrt > 1.2:
                ud_state=0
                print("too low")
                myDrone.move_up(20)
                time.sleep(1)                
            elif yrt < 0.7:
                ud_state=0
                print("too high")
                myDrone.move_down(20)
                time.sleep(1)                
            else:
                ud_state=1
                print("height stable")

            #scale the balance of far and close and move the drone   
            if faces[0][2] * faces[0][3] < 20000:
                fs_state=0
                print("too far!")
                myDrone.move_forward(20)
                time.sleep(1)
            elif faces[0][2] * faces[0][3] > 50000:
                fs_state=0
                print("too close!")
                myDrone.move_back(20)
                time.sleep(1)
            else:
                print("farness stable")
                fs_state=1
            
            if lr_state and ud_state and fs_state == 1:
                stable_state = 1
                print("perfectly stable.")
            else:
                stable_state = 0
            
        else:
            print("too much face")
            if movefb % 2 == 0:                
                myDrone.move_back(40)
                time.sleep(1)
            else:
                myDrone.move_forward(40)
                time.sleep(1)
            movefb += 1

# 4-cuts photo
if cnt > 4:
    for i in range(cnt/4):

        imgur = 'C:\\Users\\harry\\Desktop\\drone\\screenshot{}.png'.format(i*4-4)
        imgul = 'C:\\Users\\harry\\Desktop\\drone\\screenshot{}.png'.format(i*4-3)
        imglr = 'C:\\Users\\harry\\Desktop\\drone\\screenshot{}.png'.format(i*4-2)
        imgll = 'C:\\Users\\harry\\Desktop\\drone\\screenshot{}.png'.format(i*4-1)

        img1 = cv2.imread(imgur,1)
        img2 = cv2.imread(imgul,1)
        img3 = cv2.imread(imglr,1)
        img4 = cv2.imread(imgll,1)

        img1 = cv2.resize(img1,(230,260))
        img2 = cv2.resize(img2,(230,260))
        img3 = cv2.resize(img3,(230,260))
        img4 = cv2.resize(img4,(230,260))

        img5 = cv2.vconcat([img1, img2])
        img6 = cv2.vconcat([img3, img4])

        img7 = cv2.hconcat([img5,img6])

        cv2.imwrite('concatimg{}.png'.format(i),img7)


exit(0)

