from functions import *

# GRID is 45x45? px

# pos = [i for i in pyautogui.locateOnScreen('easy_grid.png')]  # Must be new board
# pos = [left, top, width, height]


# pos = [1207, 421, 450, 360]  # Home Computer
pos = [1027, 385, 450, 360]  # School Computer

grid = grid(pos)
x = getcoords(pos, 1, 1)
print(pyautogui.pixel(int(x[0]), int(x[1])))
[print(*row) for row in grid]

idx1 = 0
idx2 = 0
for i in grid:
    for j in i:
        # print(j)
        if j != ' ' and j != '-':  # or j == flag...
            adjs = adjacents(grid, idx1, idx2)
            if grid[idx1][idx2] == str(adjs.count('-')):
                # print("yes")
                print(getcoords(pos, idx1, idx2))

        idx2 += 1
    # if number of empty squares equals number of bombs then bomb must be those squares
    idx1 += 1
    idx2 = 0
