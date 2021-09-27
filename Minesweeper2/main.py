from functions import *

pos = [1027, 385, 450, 360]  # School Computer
# pos = [1207, 421, 450, 360]  # Home Computer

board1 = grid(pos)
temp = board1
for row in range(len(temp)):
    for item in range(row):
        if temp[row][item] != ' ' and temp[row][item] != '-':
            adjs = adjacents(temp, row, item)
            if temp[row][item] == str(adjs.count('-')):
                unopened(row, temp, adjs, 'flagAll')

[print(*row) for row in board1]
