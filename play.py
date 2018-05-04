from Board import Board, T, Player
from State import Position
from MCTS import MonteCarloTreeSearch


def play_vs_AI(n=3):
    board = Board()
    player = Player(T.X)
    mcts = MonteCarloTreeSearch()
    
    board.perform_move(player, Position(0,0))
    board.print_board()

    mcts.find_next_move(board, player)

play_vs_AI()