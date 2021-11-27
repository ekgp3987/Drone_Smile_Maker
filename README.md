# Smile_maker
Drone and Robotics class project using Tello Drone & python & openCV

<h2> 1. Project description </h2>
  "Smile Maker" can make you smile
 
 <h2> 2. Features </h2>
  - Track your face </br>
  - Take a photo when you smile </br>
  - Make a photo book with taken photo</br>

 <h2> 3. Implement algorithm </h2>
  Haar Cascade classifier </br>

  - Method for recognize specific object is compare an image with certain features </br>
  - For face recognition we use Haar feature  Which check the  brightness difference of pixels </br>

 Block diagram
 ![blockdiagram](https://user-images.githubusercontent.com/57945707/143688774-5b97f320-9d4a-4798-b10d-35673bad90fe.PNG)
 
 <h2> 3.1 Face Tracking </h2> 
 when it take off, divide in three situation, If there is more than one face, move the drone back and forward until it find the faces.
If there is no face, start the face finding algorithm which is moving like a snail I keep moving wider and wider, when face is detected and there is only one face, adjust the horizontal, vertical, and distance.
Adjusting horizontal and vertical is calibrating the coordinate value and make a ratio to calculate to whether it in the side or in the middle. 

 <h2> 3.2 Taking a photo when it smile</h2> 
 When it smile, it take a screen shot. 
For the smile detection we extract face recognition image and recognize the smile in that specific area.
If there is smile, we use open cv’s function imwrite() to save screenshots.

 
 <h2> 3.3 Making 4-cuts photo</h2> 
 When program is finished, it make a four-cut photo. 
The process is working with opencv’s method. We use hconcat() and vconcat() to combine all four images.
Image also saves as cv’s imwrite() function.
The process repeats as many times as possible of four .


 
  <h2> 4. Reference </h2>
  -Face Dectection with Haar Cascade <br>
  https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08 <br>
  - 초보자를 위한 Python으로 실시간 AI미소 감지기 구축 (튜토리얼) <br>
  https://www.youtube.com/watch?v=uLY5JSE5WAU <br>
  - Face XML file <br>
  https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml <br>
  - Smile XML file <br>
  https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_smile.xml <br>

