import cv2
import os

images = os.listdir('image')
n = 0
while True:
    # print(f'image/{images[n]}')
    img = cv2.imread(f'image/{images[n]}')
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == ord('+'):
        n += 1
        if n >= len(images):
            n = 0
    #
    # cv2.imshow('img', img)
    # time = datetime.now().strftime('%y%m%d %H%M%S.png')
    # namefile = f'image/{time}.png'
    #
    #
