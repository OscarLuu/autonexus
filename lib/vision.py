import cv2
import numpy as np

class Vision:

    def __init__(self, image_path: str, debug: bool=False):
        self.stats = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.stats_w = self.stats.shape[1]
        self.stats_h = self.stats.shape[0]
        self.debug = debug

    def process_screenshot(self, image):
        result = cv2.matchTemplate(image, self.stats, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= .65)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.stats_w, self.stats_h]

            rectangles.append(rect)

        if self.debug:
            line_color = (0, 255, 0)
            line_type = cv2.LINE_4
            for (x, y, w, h) in rectangles:
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                cv2.rectangle(image, top_left, bottom_right, color=line_color,
                lineType=line_type, thickness=2)

        return image