import random
from Board import Board, Player, Position

# board = [[i+2*j for j in range(5)] for i in range(5)]
# print(board)
# i = 3
# j = 3
# print([board[i][j] for i in range(5)], [board[i][j] for j in range(5)])

p1 = Player('X')
p2 = Player('O')
p = p1
b = Board()
pos = Position(1,2)
b.perform_move(p1, pos)
b.print_board()
b.print_board(mode='symb')

for i in range(9):
    p = p1 if p == p2 else p2
    m = random.randint(0, 2)
    n = random.randint(0, 2)
    pos = Position(m, n)
    while b.perform_move(p, pos) == -1:
        m = random.randint(0, 2)
        n = random.randint(0, 2)
        pos = Position(m, n)
    b.print_board()
    r = b.check_status()
    if r > 0:
        b.print_status()
        break