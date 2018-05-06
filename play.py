from Board import Board, T, Player
from State import Position
from MCTS import MonteCarloTreeSearch


def play_vs_AI(n=3):
    board = Board()
    player = Player(T.X)
    mcts = MonteCarloTreeSearch()
    
    # board.perform_move(player, Position(0,0))
    # board.print_board()
    
    print('AI turn:')
    board.print_board()
    while board.check_status() == T.E:
        print('[play.py]:', T.num_to_symbol[board.check_status()])
        board = mcts.find_next_move(board, player)
        board.print_board()

play_vs_AI()