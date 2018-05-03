import sys
from math import sqrt, log
from State import State, Node


def uct(parent_visit, node_win_count, node_visit):
    if node_visit == 0:
        return sys.maxsize

    return node_win_count/node_visit + 1.41*sqrt(log(parent_visit) / node_visit)

def find_best_node_uct(parent_node):
    parent_visit = parent_node.state.visit_count
    max_child_node = None
    max_uct_score = -sys.maxsize
    for child_node in parent_node.children:
        uct_score = uct(parent_visit, child_node.state.win_score, child_node.state.visit_count)
        if uct_score > max_uct_score:
            max_uct_score = uct_score
            max_child_node = child_node

    return max_child_node

def expand_node(parent_node):
    possible_states = parent_node.state.get_all_possible_states()
    for state in possible_states:
        # new node requires:
        # .state: board and player
        # .parent
        new_node = Node(parent_node, state)
        parent_node.children.append(new_node)
        Node.node_count += 1
