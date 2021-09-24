from functions import *

pos = [1027, 385, 450, 360]
board = grid(pos)

for row in range(len(board)):
    for cell in range(len(board[row])):
        item = board[row][cell]
        if item != '-' and item != ' ' and item != 'P':
            adj = adjacents(board, row, cell)
            if item == str(adj.count('-')):
                board = unopened(pos, board, row, cell, adj, 'flagAll')

for row in range(len(board)):
    for cell in range(row):
        item = board[row][cell]
        if item != '-' and item != ' ' and item != 'P':
            adj = adjacents(board, row, cell)
            if item == str(adj.count('-') + adj.count('P')):
                board = unopened(pos, board, row, cell, adj, 'openAll')

