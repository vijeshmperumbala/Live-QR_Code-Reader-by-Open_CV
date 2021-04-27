import cv2
import numpy as np
from pyzbar.pyzbar import decode

image = cv2.imread('C:\\Users\\BigBlue\\Documents\\project\\Live QRCode_Reader\\Live-QR_Code-Reader-by-Open_CV\\qrcode.png')

# decode = decode(image)
# print(decode)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,image = cap.read()
    
    code = decode(image)
    for img in code:
        text = img.data.decode('utf-8')
        points = np.array([img.polygon],np.int32)
        cv2.polylines(image, [points],True, (0, 255, 0), 2,)
        print(text)



    cv2.imshow('Output Image',image)
    cv2.waitKey(2)