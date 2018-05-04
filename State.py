"""
Reference: http://www.baeldung.com/java-monte-carlo-tree-search
"""
import random
from Board import Player, Board, Position, T


class State():
    def __init__(self, board, player, visit_count=0, win_score=0):
        self.board = board              # Board board;
        self.player = player            # int player; // X is 1, O is 2
        self.visit_count = visit_count  # number of times this node visited
        self.win_score = win_score      # sum of count of winning child nodes

    def get_all_possible_states(self):
        availible_positions = self.board.get_empty_positions()
        # print('[State.get_all_possible_states]:', availible_positions)
        possible_states = []

        for position in availible_positions:
            player = Player(T.X) if self.player == Player(T.O) else Player(T.O)
            new_state = State(self.board, player)
            new_state.board.perform_move(player, position)
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

    def get_opponent(self):
        return T.opponent_of(self.player)
    
    def toggle_player(self):
        self.player = self.get_opponent()

class Node():
    node_count = 0
    def __init__(self, state, parent, children=[]):
        self.state = state
        self.parent = parent
        self.children = children

    def add_child(self, child_node):
        self.children.append(child_node)
        Node.node_count += 1

    def get_random_child(self):
        k = random.randint(0, self.child_count()-1)
        return self.children[k]

    def get_child_with_max_score(self):
        """
        Source: 
        https://stackoverflow.com/questions/13067615/python-getting-the-max-value-of-y-from-a-list-of-objects?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
        returns argmax(node.visit_count)
        """
        return max(self.children, key=lambda child: child.state.visit_count)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.child_count() == 0

    def child_count(self):
        return len(self.children)

    @classmethod
    def deep_copy(cls, node):
        return cls(node.state, node.parent, node.children)

class Tree():
    def __init__(self, root):
        self.root = root
