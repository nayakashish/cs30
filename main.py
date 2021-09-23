from functions import *

# GRID is 45x45? px

# pos = [i for i in pyautogui.locateOnScreen('easy_grid.png')]  # Must be new board
# pos = [left, top, width, height]


# pos = [1207, 421, 450, 360]  # Home Computer
pos = [1027, 385, 450, 360]  # School Computer

grid = grid(pos)

[print(*row) for row in grid]

idx1 = 0
idx2 = 0
for i in grid:
    for j in i:
        # print(j)
        if j != ' ' and j != '-' and j != 'P':
            adjs = adjacents(grid, idx1, idx2)
            if j == str(adjs.count('P') + adjs.count('-')):
                # if cell number == number of unopened cells...
                # Get those cells and flag them.
                # if cell number == number of unopened cells and flags...
                unopened(grid, idx1, idx2, adjs, 'flagAll')
                pass
            elif j == str(adjs.count('P')):
                # all unopened cells can be opened as they cannot be bombs.
                pass
            else:
                pass

        idx2 += 1
    # if number of empty squares equals number of bombs then bomb must be those squares
    idx1 += 1
    idx2 = 0

print('')
[print(*row) for row in grid]
