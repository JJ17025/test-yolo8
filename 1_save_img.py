from datetime import datetime

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1500)

print(cap.get(3))

while True:
    _, img = cap.read()
    cv2.imshow('img', img)
    time = datetime.now().strftime('%y%m%d %H%M%S')
    namefile = f'image/{time}.png'

    cv2.imwrite(namefile,img)
    cv2.waitKey(1)
