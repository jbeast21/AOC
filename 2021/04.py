# Day 4

import numpy as np

fn = 'input.txt'
f = open(fn)
bingo_nums = [int(x) for x in f.readline().strip().split(',')]
f.readline()

allboards = []
board = []
for line in f:
    if line.strip():
        board.append([int(x) for x in line.strip().split()])
    else:
        allboards.append(np.array(board).astype('float'))
        board = []


def calcScore(board, num):
    return(int(np.nansum(board)*num))


def markBoard(board, num):
    board[board == num] = np.nan
    return(board)


def isWinner(board):
    if checkCols(board):
        return(True)
    elif checkCols(np.transpose(board)):
        return(True)
    return(False)


def checkCols(board):
    for col in range(len(board)):
        if np.count_nonzero(~np.isnan(board[:, col])) == 0:
            return(True)
    return(False)


allboards_marked = allboards.copy()
winners = []
for num in bingo_nums:
    for i in range(len(allboards_marked)):
        if i in winners:
            continue
        allboards_marked[i] = markBoard(allboards_marked[i], num)
        if isWinner(allboards_marked[i]):
            winners.append(i)
            if len(winners) == 1:
                print('Part 1:', calcScore(allboards_marked[i], num))
            if len(winners) == len(allboards):
                print('Part 2:', calcScore(allboards_marked[i], num))

