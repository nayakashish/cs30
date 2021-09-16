from functions import *

[print(*row) for row in grid()]

for row in grid():
    for cell in row:
        if cell == ' ':
            pass
        if cell == '1'