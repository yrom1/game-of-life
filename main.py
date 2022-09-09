"""
https://leetcode.com/problems/game-of-life/
According to Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John
Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial
state: live (represented by a 1) or dead (represented by a 0). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

    - Any live cell with fewer than two live neighbors dies as if caused by
    under-population.
    - Any live cell with two or three live neighbors lives on to the next
    generation.
    - Any live cell with more than three live neighbors dies, as if by
    over-population.
    - Any dead cell with exactly three live neighbors becomes a live cell,
    as if by reproduction.

The next state is created by applying the above rules simultaneously to ever
cell in the current state, where births and deaths occur simultaneously.
Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

import os
import sys
from collections import Counter
from itertools import product
from time import sleep
from typing import List

import numpy as np


def gameOfLife() -> None:
    global board
    m, n = len(board), len(board[0])
    alive = set([(i, j) for i, j in product(range(m), range(n)) if board[i][j] == 1])
    neighbors = list(product(range(-1, 2), range(-1, 2)))

    count = Counter()

    for i, j in alive:
        for dx, dy in neighbors:
            count[(i + dx, j + dy)] += 1

    for x, y in count:
        if 0 <= x < m and 0 <= y < n:
            if count[x, y] == 3 and board[x][y] == 0:
                board[x][y] = 1
            if count[x, y] not in [3, 4]:  # [2, 3], but count includes itself
                board[x][y] = 0


if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)
    N = 30
    board = np.random.randint(0, 2, size=N**2).reshape(N, N).tolist()
    for i in range(N):
        os.system("clear")
        print(np.array(board))
        sleep(0.25)
        gameOfLife()
