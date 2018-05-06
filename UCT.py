import sys
from math import sqrt, log
from State import State, Node

__all__ = ['uct', 'find_best_node_uct']

def uct(parent_visit, node_win_count, node_visit):
    if node_visit == 0:
        return sys.maxsize
    if parent_visit == 0:
        # raise ValueError('Parent visit was zero! this should not happen if this node is called.')
        return -sys.maxsize

    try:
        return node_win_count/node_visit + 1.41*sqrt(log(parent_visit) / node_visit)
    except ValueError as ve:
        print('ValueError:', ve)
        print('parent_visit:', parent_visit, 'node_win_count:', node_win_count, 'node_visit:', node_visit)
        raise ValueError

def find_best_node_uct(parent_node):
    parent_visit = parent_node.state.visit_count
    max_child_node = None
    max_uct_score = -sys.maxsize
    for child_node in parent_node.children:
        uct_score = uct(parent_visit, child_node.state.win_score, child_node.state.visit_count)
        if uct_score > max_uct_score:
            max_uct_score = uct_score
            max_child_node = child_node

    print('[UCT.find_best_node_uct]:', max_uct_score, max_child_node)
    return max_child_node

