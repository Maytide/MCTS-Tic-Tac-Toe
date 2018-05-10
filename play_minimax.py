import random
from Minimax.minimax import Minimax
from Board import Board, T, Position


def AI_vs_AI(n=3, mode='regular'):
    board = Board()
    player = T.X
    minimax = Minimax()

    board.print_board()
    while board.check_status() == T.E:
        print('[play_minimax.py]:', T.num_to_symbol[board.check_status()])
        _, board = minimax.find_next_move(board, player, mode=mode)
        player = T.opponent_of(player)
        board.print_board()

print('Regular play:')
AI_vs_AI(mode='regular')
print('Reverse play:')
AI_vs_AI(mode='reverse')