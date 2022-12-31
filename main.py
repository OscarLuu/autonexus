import cv2
from time import time
import numpy as np

from lib.capture import RotMGCapture
from lib.vision import Vision


capture = RotMGCapture()
vision = Vision("static/stats.png", debug=True)
loop_time = time()
while(True):
    screenshot = capture.get_screenshot()
    cv2.imshow('result', vision.process_screenshot(screenshot))
    #vision.process_screenshot(screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
