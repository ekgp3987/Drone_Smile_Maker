import cv2

imgur = 'C:\\Users\\harry\\Desktop\\drone\\screenshot0.png'
imgul = 'C:\\Users\\harry\\Desktop\\drone\\screenshot1.png'
imglr = 'C:\\Users\\harry\\Desktop\\drone\\screenshot2.png'
imgll = 'C:\\Users\\harry\\Desktop\\drone\\screenshot3.png'

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

cv2.imshow('concatimg.png',img7)
cv2.imwrite('concatimg.png',img7)