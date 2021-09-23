import pyautogui
import time



def screenshot(left, top, width, height, title=''):
    if title == '':
        image = pyautogui.screenshot(region=(left, top, width, height))
    else:
        image = pyautogui.screenshot(title, region=(left, top, width, height))
    return image


def adjacents(lst, idx1, idx2):
    adj = []
    for q in range(8):
        i = idx1
        j = idx2

        if q == 0:
            i -= 1
            j -= 1
        elif q == 1:
            i -= 1
        elif q == 2:
            i -= 1
            j += 1
        elif q == 3:
            j -= 1
        elif q == 4:
            j += 1
        elif q == 5:
            i += 1
            j -= 1
        elif q == 6:
            i += 1
        elif q == 7:
            i += 1
            j += 1

        if i < 0 or i > 7:
            adj.append('/')
        elif j < 0 or j > 9:
            adj.append('/')  # Slash means index out of bounds.
        else:
            adj.append(lst[i][j])
    return adj


def classify(x, y):
    y = int(y)
    x = int(x)
    if pyautogui.pixelMatchesColor(x, y - 4, (182, 188, 68), tolerance=40):
        icon = '-'  # I DONT UNDERSTAND WHY IT WORKS, IT JUST DOES
        # print(pyautogui.pixel(x, y))
    elif pyautogui.pixelMatchesColor(x, y, (162, 208, 73), tolerance=20):
        icon = 'P'
    elif pyautogui.pixelMatchesColor(x, y, (215, 184, 153), tolerance=20):
        icon = ' '
    elif pyautogui.pixelMatchesColor(x, y, (25, 118, 211), tolerance=20):
        icon = '1'
    elif pyautogui.pixelMatchesColor(x, y, (57, 142, 61), tolerance=65):
        icon = '2'
    elif pyautogui.pixelMatchesColor(x, y, (208, 48, 47), tolerance=20):
        icon = '3'
    elif pyautogui.pixelMatchesColor(x, y, (143, 64, 161), tolerance=20):
        icon = '4'
    else:
        icon = '!'
        print(x, y)
        print(pyautogui.pixel(x, y))

        # print(rgb)

    return icon


def grid(pos):
    left = pos[0] + 23
    top = pos[1] + 23
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


def unopened(board, idx1, idx2, adjs, action):
    if action == 'flagAll':
        for i in range(len(adjs)):
            temp1 = idx1
            temp2 = idx2
            if adjs[i] == '-':
                if i == 0:
                    temp1 -= 1
                    temp2 -= 1
                elif i == 1:
                    temp1 -= 1
                elif i == 2:
                    temp1 -= 1
                    temp2 += 1
                elif i == 3:
                    temp2 -= 1
                elif i == 4:
                    temp2 += 1
                elif i == 5:
                    temp1 += 1
                    temp2 -= 1
                elif i == 6:
                    temp1 += 1
                elif i == 7:
                    temp1 += 1
                    temp2 += 1

                board[temp1][temp2] = 'P'
                # fix thisss
            else:
                continue
    if action == 'openAll':
        for i in range(len(adjs)):
            temp1 = idx1
            temp2 = idx2
            if adjs[i] == '-':
                if i == 0:
                    temp1 -= 1
                    temp2 -= 1
                elif i == 1:
                    temp1 -= 1
                elif i == 2:
                    temp1 -= 1
                    temp2 += 1
                elif i == 3:
                    temp2 -= 1
                elif i == 4:
                    temp2 += 1
                elif i == 5:
                    temp1 += 1
                    temp2 -= 1
                elif i == 6:
                    temp1 += 1
                elif i == 7:
                    temp1 += 1
                    temp2 += 1

                coords = getcoords(temp1, temp2)
                pyautogui.click(x=coords[0], y=coords[1])

                # fix thisss
            else:
                continue
    return board


def getcoords(idx1, idx2):  # list of board, screen coords, index of row, and column
    import main
    pos = main.pos
    x = pos[0] + (45 * idx2)
    y = pos[1] + (45 * idx1)

    return int(x + 22.5), int(y + 22.5)
    # [/, /, /, -, '', -, 2, '']
    # 0           i -= 1
    # 0           j -= 1
    # 1           i -= 1
    # 2           i -= 1
    # 2           j += 1
    # 3           j -= 1
    # 4           j += 1
    # 5           i += 1
    # 5           j -= 1
    # 6           i += 1
    # 7           i += 1
    # 7           j += 1


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
