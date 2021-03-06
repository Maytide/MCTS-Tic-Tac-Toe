from Board import Board, T
from State import Position
from MCTS.MCTS import MonteCarloTreeSearch


def AI_vs_AI(n=3):
    board = Board()
    player = T.X
    mcts = MonteCarloTreeSearch()
    
    # board.perform_move(player, Position(0,0))
    # board.print_board()
    # 1 + 2

    print('AI turn:')
    board.print_board()
    while board.check_status() == T.E:
        print('[play_mcts.py]:', T.num_to_symbol[board.check_status()])
        tree, board = mcts.find_next_move(board, player)
        player = T.opponent_of(player)
        board.print_board()
        # tree.print_tree_boards()
        pass


def player_vs_AI(n=3):
    board = Board()
    player = T.X
    mcts = MonteCarloTreeSearch()

    board.print_board()
    for move in range(9):
        if move % 2 == 0:
            input_position = input('Enter move in form [i j]:')
            i, j = [int(k) for k in input_position.split(' ')]
            pos = Position(i, j)
            board.perform_move(player, pos)
        else:
            tree, board = mcts.find_next_move(board, player)

        if board.check_status() == T.X:
            print('You win!')
            board.print_board()
            break
        elif board.check_status() == T.O:
            print('You lose!')
            board.print_board()
            break

        board.print_board()
        player = T.opponent_of(player)

AI_vs_AI()
# player_vs_AI()