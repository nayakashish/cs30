import pyautogui


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
        icon = '-'
    elif pyautogui.pixelMatchesColor(x, y, (162, 208, 115), tolerance=25):
        icon = 'P'
    elif pyautogui.pixelMatchesColor(x, y, (215, 184, 153), tolerance=20):
        icon = ' '
    elif pyautogui.pixelMatchesColor(x, y, (25, 118, 211), tolerance=20):
        icon = '1'
    elif pyautogui.pixelMatchesColor(x, y, (57, 142, 61), tolerance=65):
        icon = '2'
    elif pyautogui.pixelMatchesColor(x, y, (208, 48, 47), tolerance=20):
    # elif pyautogui.pixelMatchesColor(x, y, (214, 150, 127), tolerance=25):
        icon = '3'
    elif pyautogui.pixelMatchesColor(x, y, (143, 64, 161), tolerance=20):
        icon = '4'
    elif pyautogui.pixelMatchesColor(x, y, (255, 143, 0), tolerance=20):
        icon = '5'
    else:
        icon = '!'
        print('Unrecognized Cell @ {}, {}. \nColour Code: {}'.format(x, y, pyautogui.pixel(x, y)))
        exit()

    return icon


def grid(pos):
    left = pos[0] + 23
    top = pos[1] + 23
    lst = []
    templst = []
    for j in range(8):

        for i in range(10):
            templst.append(classify(left, top))

            left += 45
        lst.append(templst)
        templst = []
        top += 45
        left = pos[0] + 23

    return lst


flaglst = []
openlst = []


def unopened(idx1, idx2, adjacent, action):
    for i in range(len(adjacent)):
        temp1 = idx1
        temp2 = idx2
        if adjacent[i] == '-':
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

            if action == 'flagAll':
                if [temp1, temp2] not in flaglst:
                    flaglst.append([temp1, temp2])
            elif action == 'openAll':
                if [temp1, temp2] not in openlst:
                    openlst.append([temp1, temp2])

    if action == 'flagAll':
        return flaglst
    elif action == 'openAll':
        return openlst


def update_board(board, cells_to_update, new_icon):  # cells to update must be list
    for value in cells_to_update:
        board[value[0]][value[1]] = new_icon
    return board


def count_flags(lst):
    count = 10
    for i in lst:
        for j in i:
            if j == 'P':
                count -= 1
    return count


def click_cells(pos, lst_cells, button='left'):
    for i in lst_cells:
        x = pos[0] + (45 * i[1])
        y = pos[1] + (45 * i[0])
        pyautogui.click(x + 23, y + 23, button=button)
    openlst.clear()
    flaglst.clear()

    # pyautogui.moveTo(1025, 330)
    return
