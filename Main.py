import cv2
import numpy as np
from pyzbar.pyzbar import decode

# reading live video from camera
cap = cv2.VideoCapture(0)
# setting width 640px
cap.set(3,640)
# setting height 480px
cap.set(4,480)

# reading continous image from camera and decode the QR code from it
while True:
    # reading reach image and decode the points of QR code from image
    success,image = cap.read()
    code = decode(image)
    # reading data from QR code
    for img in code:
        text = img.data.decode('utf-8')
        # reading polygon coordinates for draw rectangle box over QR code
        points = np.array([img.polygon],np.int32)
        # reading recangle coordinates for place text behaind the box
        rect = img.rect
        # drawing the rectangle box / we use polygon to better 
        cv2.polylines(image, [points],True, (0, 255, 0), 2,)
        # putting text over the box
        cv2.putText(image,text,(rect[0], rect[1]),cv2.FONT_HERSHEY_PLAIN,1.5, (0,250,0),2)

    # showing the result video
    cv2.imshow('Output Image',image)
    # Enter key q to exit from video outputfram
    if cv2.waitKey(2) == ord('q'):
        break

# closing all the cv2 windows 
cap.release()
cv2.destroyAllWindows()