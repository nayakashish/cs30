import time
from random import randrange

from functions import *

#pos = [1027, 385, 450, 360]  # School Computer
#
pos = [982, 356, 540, 420]

# pos = [1207, 421, 450, 360]  # Home Computer

# Scan BOARD

def run(pos):
    count = 0
    board1 = grid(pos)
    temp = board1

    [print(*row) for row in temp]
    # Flag CELLS
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            cell = temp[i][j]
            if cell != ' ' and cell != '-':
                adjs = adjacents(temp, i, j)
                if cell == str(adjs.count('-')):
                    t = unopened(i, j, adjs, 'flagAll')
    # Update board
    temp = update_board(board1, t, 'P')
    # open and click cells
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            cell = temp[i][j]
            if cell != ' ' and cell != '-':
                adjs = adjacents(temp, i, j)
                if cell == str(adjs.count('P')):
                    y = unopened(i, j, adjs, 'openAll')

    # RAISE CALL BEFORE ASSIGNMENT EXCEPT....
    click_cells(pos, y)

    count += len(t)
    print()
    if count < 10:
        run(pos)
    else:
        [print(*row) for row in temp]
        return

    # print(y)


#x = randrange(10)
#y = randrange(8)
#click_cells(pos, [[x, y]])
# pyautogui.moveTo(1045, 180)
#time.sleep(1)
run(pos)
