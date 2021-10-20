from utils import *
import time
import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
cnt = 1
face_on = 0 

if __name__ == "__main__":
    myDrone = initTello()    
    myDrone.streamon() 
    time.sleep(2)  
    frame_read = myDrone.get_frame_read()
    time.sleep(2)
    myDrone.takeoff()
    time.sleep(2)

    while True:

        img = frame_read.frame
       
        # Change to grayscale
        frame_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces first
        faces = face_detector.detectMultiScale(frame_grayscale)

        # Check the faces wether there is no faces at firts, go up until find faces
        if not list(faces):
            print("no face! move up!")
            myDrone.move_up(20)
            time.sleep(1)


        # Run face detector within each of those faces
        for (x, y, w, h) in faces:

            # Check the size of faces
            print("size is {}".format(w*h))

            # Draw a rectangle around the face
            cv2.rectangle(img, (x,y), (x+w, y+h), (100, 200, 50), 4)

            # Check the size of faces 
            if (w*h<20000):
                print("size small move for!")
                myDrone.move_forward(20)
                time.sleep(1)
        
            # Get the sub frame (using numpy)
            the_face = img[y:y+h, x:x+w]    

            # Change to gray Scale
            face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

            # Run smile Detector on sub frame with some factors (to recognize more accurate)
            smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)            

            # Check the smile
            if len(smiles) > 0:
                print("it smile!")
                print("Screenshot saved...")
                cv2.imwrite('screenshot{}.png'.format(cnt), img) # Save Screen shot with cv method
                cnt += 1        
        
        # Show the corrent frame
        cv2.imshow("drone",img)

        # Keep update the frame and wait for keyboard input
        keyboard = cv2.waitKey(1)

        if keyboard & 0xFF == ord('q'):
            myDrone.land()
            frame_read.stop()
            myDrone.streamoff()
            exit(0)
            break

        if keyboard & 0xFF == ord('f'):
            myDrone.flip_back()
            time.sleep(1)          

        if keyboard & 0xFF == ord('w'):
            myDrone.move_forward(20)
            time.sleep(1)          

        if keyboard & 0xFF == ord('s'):
            myDrone.move_back(20)
            time.sleep(1)

        if keyboard & 0xFF == ord('d'):
            myDrone.move_down(20)
            time.sleep(1)

         