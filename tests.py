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
pos = [1027, 385, 448, 359] # School Computer
# pos = [1207, 421, 450, 360]  # Home Computer


left = 23
top = 22.5
shot = screenshot(pos[0], pos[1], pos[2], pos[3])
lst = []
templst = []
for j in range(8):

    for i in range(10):
        icon = ''
        rgb = shot.getpixel((left, top))
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
        else:
            icon = '!'


        templst.append(icon)


        left += 45
    lst.append(templst)
    templst = []
    top += 45
    left = 23

[print(*row) for row in lst]

''' 
Colour Codes RGB
Three 211 47 47
Two 118 161 96 or (113, 157, 94)
One 25 118 210
Four
Five
Six
Seven
Eight


Bkg1 170 215 81
Bkg2 162 209 73

Empty1 229 194 159
Empty2 215 184 153
'''
