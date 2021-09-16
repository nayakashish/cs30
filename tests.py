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
print(lst)
for j in range(8):

    for i in range(10):

        # screenshot(left, top, 45, 45, '{}.png'.format(num))
        templst.append(shot.getpixel((left, top)))


        left += 45
    lst.append(templst)
    templst = []
    top += 45
    left = 23

print(lst)
''' 
Colour Codes RGB
Three 211 47 47
Two 118 161 96
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
