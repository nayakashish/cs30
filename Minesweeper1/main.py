import functions

# GRID cells are 45x45px

# pos = [i for i in pyautogui.locateOnScreen('easy_grid.png')]  # Must be new board
# pos = [left, top, width, height]


#pos = [1207, 421, 450, 360]  # Home Computer

pos = [1027, 385, 450, 360]  # School Computer

grid = functions.grid(pos)


def main(grid):
    for row in grid:
        if row.count('!') > 0:
            print('\nUnrecognized Cell')
            [print(*row) for row in grid]
            exit()

    idx1 = 0
    idx2 = 0
    for row in grid:
        for item in row:
            # print(item)
            if item != ' ' and item != '-' and item != 'P':
                adjs = functions.adjacents(grid, idx1, idx2)
                if item == str(adjs.count('P') + adjs.count('-')):
                    # if cell number == number of unopened cells...
                    # Get those cells and flag them.
                    # if cell number == number of unopened cells and flags...
                    functions.unopened(pos, grid, idx1, idx2, adjs, 'flagAll')

                elif item == str(adjs.count('P')):
                    # all unopened cells can be opened as they cannot be bombs.
                    # if action openall
                    functions.unopened(pos, grid, idx1, idx2, adjs, 'openAll')

                else:
                    pass

            idx2 += 1
        # if number of empty squares equals number of bombs then bomb must be those squares
        idx1 += 1
        idx2 = 0
        [print(*row) for row in grid]
        print('\n')

    return grid


# loop:
#    scan grid
#    read cells add to master list of what to click
#    click on all cells from list

new_grid = main(grid)

count = 0
for i in main(new_grid):
    for u in i:
        if u == 'P':
            count += 1


print(count)
# print('')
print('hello')
