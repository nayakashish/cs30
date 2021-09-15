import pyautogui
import time


def screenshot(left, top, width, height):
    im1 = pyautogui.screenshot('testimage.png', region=(left, top, width, height))
    return im1

# GRID is 45x45? px

# pos = [i for i in pyautogui.locateOnScreen('easy_grid.png')]
# print(pos)

print('Yes')
# time.sleep(3)

# screenshot(pos[0], pos[1], pos[2], pos[3])
# left 1162 top 520 45 45
d = screenshot(1387, 430, 45, 45)
print(d.getpixel((23, 22.5)))


# Red 211 47 47
