import cv2
import numpy as np
import win32gui, win32ui, win32con

class RotMGCapture:

    w = 0
    h = 0
    hwnd = None

    def __init__(self):
        self.hwnd = None

        left, top, right, bottom = win32gui.GetWindowRect(win32gui.FindWindow(None, 'RotMGExalt'))
        self.w = right - left
        self.h = bottom - top

    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img