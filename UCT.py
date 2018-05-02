import sys
from math import sqrt, log


def uct(total_visit, node_win_count, node_visit):
    if node_visit == 0:
        return sys.maxsize

    return node_win_count/node_visit + 1.41*sqrt(log(total_visit)/node_visit)

def find_best_node_uct(node):
    parent_visit = node.state.visit_count
