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


def classicon(rgb):
    if rgb == (170, 215, 81) or rgb == (162, 209, 73):
        icon = '-'
    elif rgb == (229, 194, 159) or rgb == (215, 184, 153):
        icon = ' '
    elif rgb == (25, 118, 210):
        icon = '1'
    elif rgb == (118, 161, 96) or rgb == (113, 157, 94):
        icon = '2'
    elif rgb == (211, 47, 47):
        icon = '3'
    elif rgb == (143, 64, 160) or rgb == (146, 66, 161):
        icon = '4'
    elif rgb == (175, 183, 62) or (182, 188, 68):
        icon = 'X'
    else:
        icon = '!'
        print(rgb)
    return icon


def grid():
    left = 23
    top = 22.5
    shot = screenshot(pos[0], pos[1], pos[2], pos[3])
    lst = []
    templst = []
    for j in range(8):

        for i in range(10):
            icon = ''
            rgb = shot.getpixel((left, top))
            templst.append(classicon(rgb))

            left += 45
        lst.append(templst)
        templst = []
        top += 45
        left = 23

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
