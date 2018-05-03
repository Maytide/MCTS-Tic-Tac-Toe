from State import State, Tree, Node
from Board import Player, Board, Position, T

class MonteCarloTreeSearch():
    WIN_SCORE = 10
    def __init__(self):
        self.opponent = T.X
    
    def find_next_move(self, board, player):
        self.opponent = T.opponent_of(player)
        # tree = Tree(Node())
