"""
Reference: http://www.baeldung.com/java-monte-carlo-tree-search
"""
import random
from Board import Player, Board, Position


class State():
    def __init__(self, board, player, visit_count=0, win_score=0):
        self.board = board              # Board board;
        self.player = player            # int player; // X is 1, O is 2
        self.visit_count = visit_count  # number of times this node visited
        self.win_score = win_score      # sum of count of winning child nodes

    def get_all_possible_states(self):
        availible_positions = self.board.get_empty_positions()
        possible_states = []

        for position in availible_positions:
            player = 1 if self.player == 2 else 2
            new_state = State(self.board, player)
            new_state.board.perform_move(position, player)
            possible_states.append(new_state)

        return possible_states

    def random_play(self):
        availible_positions = self.board.get_empty_positions()
        assert len(availible_positions) > 0
        move = availible_positions[
            random.randint(0, len(availible_positions)-1)
        ]
        self.board.perform_move(move)

        return 1

    def add_score(self, score):
        self.win_score += score

    def increment_visit(self):
        self.visit_count += 1

class Node():
    node_count = 0
    def __init__(self, state, parent, children=[]):
        self.state = state
        self.parent = parent
        self.children = children

    def add_child(self, child_node):
        self.children.append(child_node)
        Node.node_count += 1

class Tree():
    def __init__(self, root):
        self.root = root
