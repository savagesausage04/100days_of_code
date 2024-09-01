import pyautogui
from PIL import Image, ImageGrab
import time

def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
    for i in range(1080, 1170):
        for j in range(830, 880):
            if data[i, j] < 130:
                click("up")
                return
    for i in range(1080, 1120):
        for j in range(780, 830):
            if data[i, j] < 100:
                click("down")
                return

    return
if __name__ == "__main__":
    print("About to start")
    time.sleep(5)
    click('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollision(data)
        # for i in range(1080, 1120):
        #     for j in range(460, 510):
        #         data[i, j] = 200
        #
        # for i in range(1080, 1200):
        #     for j in range(515, 565):
        #         data[i, j ] = 0
        #
        # image.show()
        # break