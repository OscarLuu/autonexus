import cv2
from time import time
import numpy as np

from lib.capture import RotMGCapture
from lib.vision import Vision
from lib.conductor import Conductor


capture = RotMGCapture()
vision = Vision("static/stats.png", debug=True)
conductor = Conductor("r", "f", "v")

loop_time = time()
while(True):
    screenshot = capture.get_screenshot()
    #cv2.imshow('result', vision.process_screenshot(screenshot))
    data = vision.process_screenshot(screenshot)
    conductor.conductor(data)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
