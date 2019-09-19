"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Steps to solution:
1.) Iterate through each index in 2D Array. Only count the first cell of the battleship.

2.) The first cell is the top-left cell.

3.) Check all of these 'first' cells by only counting cells that don't have an 'X' to the left and do not have an 'X' above.

"""

def countBattleships(self, board):
    M = len(board)
    N = len(board[0])
    count = 0

    if M == 0:
        return 0

    for i in range(M):
        for j in range(N):
            if board[i][j] == '.':
                continue
            if i > 0 and board[i - 1][j] == 'X':
                continue
            if j > 0 and board[i][j - 1] == 'X':
                continue
            count += 1
    return count
