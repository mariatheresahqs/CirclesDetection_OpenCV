import cv2
# from matplotlib import pyplot as plt
import numpy as np

images = ['1', '2', '3', '4', '5', '6','7']
output = 0

for i in range(len(images)):

    img = cv2.imread(images[i] + '.jpg')

    # Image treatment
    brightness = 20
    contrast = 100
    img = np.int16(img)
    img = img * (contrast/127+1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)

    # Convert an image from one color space to another
    img_cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Add median filter to image
    img_cinza = cv2.medianBlur(img_cinza, 21)

    # Finds circles in a grayscale image 
    circles = cv2.HoughCircles(img_cinza, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=15, minRadius=170, maxRadius=70)

    # Convert radius and x,y(center) coordinates to integer
    circles = np.uint16(np.around(circles))
    img = img.copy()

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),20)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(255,0,0),10)

    cv2.putText(img, str("Quantity:"+ str(len(circles[0]))) ,(100,150), cv2.FONT_HERSHEY_COMPLEX, 5,(0,255,0),20,cv2.LINE_AA)
    
    output+=1
    nameOut = 'saida' + (str(output) + '.jpg')
    cv2.imwrite(nameOut,img)

