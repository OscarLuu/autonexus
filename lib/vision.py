import cv2
import numpy as np
import pytesseract

class Vision:

    def __init__(self, image_path: str, debug: bool=False):
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
        self.stats = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.stats_w = self.stats.shape[1]
        self.stats_h = self.stats.shape[0]

        self.debug = debug

    def process_screenshot(self, image):
        result = cv2.matchTemplate(image, self.stats, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= .5)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.stats_w, self.stats_h]

            rectangles.append(rect)

        if rectangles:
            for (x, y, w, h) in rectangles:
                blur = cv2.GaussianBlur(image, (1,1), 0)
                cropped_image = blur[y: y+h, x: x+w]
                ret, glob_thresh = cv2.threshold(cropped_image, 143, 255, cv2.THRESH_BINARY)

                kernel = np.ones((2,2), np.uint8)
                dilated = cv2.dilate(glob_thresh, kernel, iterations=1)
                inverted = cv2.bitwise_not(dilated)

                if self.debug: 
                    cv2.imshow('result', inverted)

                text = pytesseract.image_to_string(inverted).split()
                health = text[2].split('/')
                mana = text[5].split('/')

                if len(health) == 2 and len(mana) == 2:
                    try:
                        health_data = dict(
                            current_hp=int(health[0]),
                            max_hp=int(health[1]),
                            current_mana=int(mana[0]),
                            max_mana=int(mana[1])
                        )
                    except ValueError as e:
                        print ("Skipping due to parse error with data: {}".format(e))
                        return None
                    except IndexError as e:
                        print ("SKipping due to list index: {}".format(e))
                        return None

                    return health_data

