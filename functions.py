import pyautogui
import time


def screenshot(left, top, width, height, title=''):
    if title == '':
        image = pyautogui.screenshot(region=(left, top, width, height))
    else:
        image = pyautogui.screenshot(title, region=(left, top, width, height))
    return image


# GRID is 45x45? px

# pos = [i for i in pyautogui.locateOnScreen('easy_grid.png')]  # Must be new board
# pos = [left, top, width, height]
pos = [1027, 385, 450, 360]  # School Computer


# pos = [1207, 421, 450, 360]  # Home Computer


def classify(x, y):
    y = int(y)
    x = int(x)
    if pyautogui.pixelMatchesColor(x, y, (162, 208, 73), tolerance=20):
        icon = '-'
    elif pyautogui.pixelMatchesColor(x, y, (215, 184, 153), tolerance=20):
        icon = ' '
    elif pyautogui.pixelMatchesColor(x, y, (25, 118, 211), tolerance=20):
        icon = '1'
    elif pyautogui.pixelMatchesColor(x, y, (57, 142, 61), tolerance=20):
        icon = '2'
    elif pyautogui.pixelMatchesColor(x, y, (208, 48, 47), tolerance=20):
        icon = '3'
    elif pyautogui.pixelMatchesColor(x, y, (143, 64, 161), tolerance=20):
        icon = '4'
    else:
        icon = '!'
        # print(rgb)

    return icon


def grid():
    left = pos[0] + 23
    top = pos[1] + 22.5
    # shot = screenshot(pos[0], pos[1], pos[2], pos[3])
    lst = []
    templst = []
    for j in range(8):

        for i in range(10):
            # rgb = shot.getpixel((left, top))
            templst.append(classify(left, top))
            # print(left, top)

            left += 45
        lst.append(templst)
        templst = []
        top += 45
        left = pos[0] + 23

    return lst


''' 
Colour Codes RGB
Three 211 47 47
Two 118 161 96 or (113, 157, 94)
One 25 118 210
Four (143, 64, 160) or (146, 66, 161)
Five
Six
Seven
Eight


Bkg1 170 215 81
Bkg2 162 209 73

Empty1 229 194 159
Empty2 215 184 153

Next TODO 
Iterate through each cell and determine if number equals unopened cells adjacent.
so first find number of unopened adjacent cells. if number equals it means the unopened cell 
is a bomb. if number of bombs found in adjacent cell flag bombs and middle click 
'''
