from functions import *

pos = [1027, 385, 450, 360]  # School Computer


# pos = [1207, 421, 450, 360]  # Home Computer

# Scan BOARD

def run(pos):
    count = 0
    board1 = grid(pos)
    temp = board1

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
    count += len(t)
    # open and click cells
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            cell = temp[i][j]
            if cell != ' ' and cell != '-':
                adjs = adjacents(temp, i, j)
                if cell == str(adjs.count('P')):
                    y = unopened(i, j, adjs, 'openAll')

    click_cells(pos, y)

    if count < 10:
        run(pos)
    else:
        [print(*row) for row in temp]
        return



    # print(y)

run(pos)


