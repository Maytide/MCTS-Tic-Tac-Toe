import random
from Minimax.minimax import Minimax
from Board import Board, T, Position


def AI_vs_AI(n=3):
    board = Board()
    player = T.X
    minimax = Minimax()

    board.print_board()
    while board.check_status() == T.E:
        print('[play_minimax.py]:', T.num_to_symbol[board.check_status()])
        _, board = minimax.find_next_move(board, player)
        player = T.opponent_of(player)
        board.print_board()

AI_vs_AI()