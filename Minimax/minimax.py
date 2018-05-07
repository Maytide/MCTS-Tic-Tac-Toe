from Board import T


class Minimax():
    def __init__(self):
        pass

    def find_next_move(self, board, player):
        move = self.minimax(board, player)
        board.perform_move(player, move['pos'])
        return 1, board

    def check_status(self, board, player):
        return board.check_status() == player

    def get_empty_positions(self, board):
        return board.get_empty_positions()

    def minimax(self, board, player):
        # print('minimax init')
        if self.check_status(board, T.X):
            minimax_move = {}
            minimax_move['score'] = -10
            return minimax_move
        elif self.check_status(board, T.O):
            minimax_move = {}
            minimax_move['score'] = +10
            return minimax_move
        elif self.check_status(board, T.D):
            minimax_move = {}
            minimax_move['score'] = 0
            return minimax_move

        availible_positions = self.get_empty_positions(board)
        moves = []

        for k, pos in enumerate(availible_positions):
            move = {}
            # board[pos.i][pos.j] = player
            board.perform_move(player, pos)
            move['pos'] = pos
            minimax_move = self.minimax(board, T.opponent_of(player))
            move['score'] = minimax_move['score']
            # board[pos.i][pos.j] = T.E
            board.unperform_move(T.E, pos)

            moves.append(move)

        if player == T.O:
            best_move = max(moves, key=lambda move: move['score'])
        else:
            best_move = min(moves, key=lambda move: move['score'])

        return best_move

