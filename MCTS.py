import sys
import time
from State import State, Tree, Node
from Board import Board, Position, T
from UCT import *


# https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
current_time = lambda: int(round(time.time()))
epsilon = 1e-6

class MonteCarloTreeSearch():
    WIN_SCORE = 10
    time_limit_per_move = 5
    def __init__(self):
        self.opponent = None #T.X
    
    def find_next_move(self, board, player):
        self.opponent = T.opponent_of(player)
        # Create new game instance. 
        # Tree with root note: no parent
        # TODO: this is creating a node with children of the same number of moves in...
        tree = Tree(Node(State(board, self.opponent), None))
        root_node = tree.root
        root_node.children = []
        root_node.state.visit_count = 1
        reference_time = current_time()

        while (current_time() - reference_time) <= (MonteCarloTreeSearch.time_limit_per_move):
            # print('[MCTS.find_nextMove]:', current_time() - reference_time, MonteCarloTreeSearch.time_limit_per_move + epsilon,)
            # -- Step 1 - Selection --
            # print('[MCTS.find_nextMove]:', root_node, root_node.children)
            if root_node in root_node.children:
                raise ValueError('Circular reference')
            promising_node = self.select_promising_node(root_node)
            # print('[MCTS.find_nextMove] - root board:', root_node.state.board.print_board())
            # print('[MCTS.find_nextMove] - promising:', promising_node.state.board.print_board())
            # -- Step 2 - Expansion -- 
            # print('[MCTS.find_nextMove] - Board status:', promising_node.state.board.check_status())
            # promising_node.state.board.print_board()
            # Why is board status == 1 so early on?
            if promising_node.state.board.check_status() == T.E:
                # game in progress
                self.expand_node(promising_node)
            
            # -- Step 3 - Simulation -- 
            exploration_node = promising_node
            if not promising_node.is_leaf():
                exploration_node = promising_node.get_random_child()

            # simulate random playout
            playout_result = self.simulate_random_playout(exploration_node)
            # -- Step 4 - Update -- 
            self.backpropogate(exploration_node, playout_result)
            # print('[MCTS.find_next_move]:')
            # exploration_node.state.board.print_board()
            # print('[MCTS.find_next_move]', exploration_node, exploration_node.children)

        # for node in root_node.children:
        #     node.state.board.print_board()
        winner_node = root_node.get_child_with_max_score()
        # print('[MCTS.find_next_move]', winner_node, winner_node.state.win_score)
        tree.root = winner_node
        return tree, winner_node.state.board

    def select_promising_node(self, root_node):
        node = root_node
        # print('[MCTS.select_promising_node]:', )
        if node in node.children:
            raise ValueError('Circular reference root')
        while not node.is_leaf():
            node = find_best_node_uct(node)
            # print('[MCTS.select_promising_node]:', node.state.visit_count, node, node.children)
            if node in node.children:
                raise ValueError('Circular reference')
        
        return node

    def expand_node(self, parent_node):
        possible_states = parent_node.state.get_all_possible_states()
        if len(possible_states) == 0: return -1
        for state in possible_states:
            # new node requires:
            # .state: board and player
            # .parent
            # new_node = Node(state, parent_node)
            new_node = Node.new_node_from_state(state)
            new_node.parent = parent_node
            new_node.state.player = parent_node.state.get_opponent()
            parent_node.add_child(new_node)
            # print('[MCTS.expand_node]:', parent_node == new_node, parent_node, parent_node.children)
            Node.node_count += 1

        return 1

    def backpropogate(self, exploration_node, player):
        temp_node = exploration_node
        while not temp_node.is_root():
            temp_node.state.increment_visit()
            if temp_node.state.player == player:
                temp_node.state.add_score(MonteCarloTreeSearch.WIN_SCORE)
            temp_node = temp_node.parent

    def simulate_random_playout(self, node):
        """
        Simulate a completely random game
        """
        temp_node = Node.new_node(node)
        temp_state = temp_node.state
        board_status = temp_state.board.check_status()

        if board_status == self.opponent:
            # opponent won ?
            temp_node.parent.state.win_score = -sys.maxsize
            return board_status
        
        while board_status == T.E:
            # while game in progress
            temp_state.toggle_player()
            temp_state.random_play()
            board_status = temp_state.board.check_status()
        # temp_state.board.print_board()
        
        return board_status
