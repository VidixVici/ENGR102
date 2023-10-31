# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Harbert, Zach Anderson
# Dhar, Arul
# Kang, Jon D
# Section: 562
# Assignment: TEAM LAB 7 go_moves.py
# Date: 4 OCTOBER 2023
#
#
# YOUR CODE HERE
#


def printBoard(board):
    for row in board:
        print(' '.join(row))
    print()

def iniboard():
    return [['.' for _ in range(9)] for _ in range(9)]

def placeStone(board, row, col, stone):
    if board[row][col] == '.':
        board[row][col] = stone
        return True
    else:
        print("Invalid move! There is already a stone at that position. Try again.")
        return False

def main():
    board = iniboard()
    current_stone = 'B'  # Black starts first

    while True:
        printBoard(board)
        move = input(f"Enter the move for {current_stone} (row col), or 'stop' to end: ")

        row, col = map(int, move.split())
        if 0 <= row < 9 and 0 <= col < 9:
            success = placeStone(board, row, col, current_stone)
            if success:
                current_stone = 'W' if current_stone == 'B' else 'B'
        else:
            print("Invalid move! Row and column should be in the range 0-8.")
       

main()