import pyautogui
from functions import *

# pos = [i for i in pyautogui.locateOnScreen('Screenshot (13).png', grayscale=True)]
pos = [982, 356, 540, 420]
print(pos)
board = grid(pos)
[print(*row) for row in board]