"""
Source implementation: https://github.com/eugenp/tutorials/blob/master/algorithms/src/main/java/com/baeldung/algorithms/mcts/tictactoe/Board.java
Reference: http://www.baeldung.com/java-monte-carlo-tree-search
"""

class T():
    E = 0  # empty square
    X = 1  # X square (or win)
    O = 2  # O square (or win)
    D = 3  # Draw
    num_to_symbol = {E: 'E', X: 'X', O: 'O', D: 'D'}
    
    @staticmethod
    def opponent_of(P):
        return T.X if P == T.O else T.O

class Position():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return '[%d, %d]' % (self.i, self.j)

# class Player():
#     def __init__(self, symbol):
#         if symbol == 'X' or symbol == 1:
#             self.P = T.X  # X
#         else:
#             self.P = T.O  # O

#     @classmethod
#     def new_player(cls, player):
#         if isinstance(player, int):
#             return cls(player)
#         elif isinstance(player, Player):
#             return cls(player.P)
#         else:
#             raise ValueError('Passed argument of type', type(player), 'to Player constructor.')

#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.P == other
#         elif isinstance(other, Player):
#             return self.P == other.P
#         else:
#             return False

class Board():
    def __init__(self, status=0, total_moves=0, n=3, board=None):
        self.status = status
        self.total_moves = total_moves
        self.n = n
        if board is None:
            self.board = [[T.E for __ in range(self.n)] for _ in range(self.n)]
        else:
            self.board = board

    @classmethod
    def new_board(cls, board):
        new_board = [[item for item in row] for row in board.board]
        return cls(board.status, board.total_moves, board.n, new_board)

    def perform_move(self, player, pos):
        if self.board[pos.i][pos.j] == T.E:
            self.total_moves += 1
            self.board[pos.i][pos.j] = player
            # self.print_board()
            return +1
        else:
            return -1

    def unperform_move(self, empty_symbol, pos):
        if self.board[pos.i][pos.j] != T.E:
            self.total_moves -= 1
            self.board[pos.i][pos.j] = empty_symbol
            # self.print_board()
            return +1
        else:
            return -1

    def get_board(self):
        return self.board

    def get_row(self, i):
        return [self.board[i][j] for j in range(self.n)]

    def get_col(self, j):
        return [self.board[i][j] for i in range(self.n)]

    def get_diag(self, dir):
        if dir == 0:
            return [self.board[i][i] for i in range(self.n)]
        else:
            return [self.board[i][self.n-i-1] for i in range(self.n)]

    def set_board(self, board):
        self.board = board

    def check_status(self):
        rdiag1 = self.check_for_win(self.get_diag(0))
        if rdiag1 != T.E:
            return rdiag1
        rdiag2 = self.check_for_win(self.get_diag(1))
        if rdiag2 != T.E:
            return rdiag2
        for i in range(self.n):
            rcol = self.check_for_win(self.get_row(i))
            if rcol != T.E:
                return rcol
            rrow = self.check_for_win(self.get_col(i))
            if rrow != T.E:
                return rrow

        return T.E if self.total_moves < 9 else T.D


    def check_for_win(self, vector):
        """
        Checks if all the elements in a row/col/diag are equal.
        https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
        """
        return vector[0] if (vector[0] != T.E) and (len(set(vector)) == 1) else T.E

    def print_board(self, mode='num'):
        print('Move number:', self.total_moves)
        for i in range(self.n):
            if mode == 'num': print(self.board[i])
            else:
                print([T.num_to_symbol[self.board[i][j]] for j in range(self.n)])
        print()

    def get_empty_positions(self):
        empty_list = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == T.E:
                    empty_list.append(Position(i,j))

        return empty_list

    def print_status(self):
        self.status = self.check_status()
        if self.status == T.E:
            print('Game in progress')
        elif self.status == T.D:
            print('Draw')
        elif self.status == T.X:
            print('X wins')
        else:
            print('O wins')