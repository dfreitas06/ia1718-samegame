#Same Game
#IA 17/18
#
#Author: Diogo Freitas   ist181586
#Author: Joao Rodrigues  ist424786

from search import * 
from utils import * 

#Provided Boards

board0 = [[2,2,1],
          [1,1,1],
          [1,1,1]]

board1 = [[1,2,1,2,1],
          [2,1,2,1,2],
          [1,2,1,2,1],
          [2,1,2,1,2]]		#4x5 board with 2 colors, no solution

board2 = [[1,2,2,3,3],
          [2,2,2,1,3],
          [1,2,2,2,2],
          [1,1,1,1,1]]		#4x5 board with 3 colors

board3 = [[3,1,3,2],
          [1,1,1,3],
          [1,3,2,1],
          [1,1,3,3],
          [3,3,1,2],
          [2,2,2,2],
          [3,1,2,3],
          [2,3,2,3],
          [5,1,1,3],
          [4,5,1,2]]		#10x4 board with 3 colors, no solution

board4 = [[3,1,3,2],
          [1,1,1,3],
          [1,3,2,1],
          [1,1,3,3],
          [3,3,1,2],
          [2,2,2,2],
          [3,1,2,3],
          [2,3,2,3],
          [2,1,1,3],
          [2,3,1,2]]		#10x4 board with 3 colors

board5 = [[1,1,5,3],
          [5,3,5,3],
          [1,2,5,4],
          [5,2,1,4],
          [5,3,5,1],
          [5,3,4,4],
          [5,5,2,5],
          [1,1,3,1],
          [1,2,1,3],
          [3,3,5,5]]		#10x4 board with 5 colors

test5 = [[1,1,3,3,3,3],
         [2,2,3,3,3,3],
         [2,2,3,3,3,3],
         [2,2,3,3,3,3],
         [2,2,3,3,3,3]]

#Color

def get_no_color():
	return 0

def no_color(c):
	return c == 0

def color(c):
	return c > 0

#Position

def make_pos(l, c):
	return (l, c)

def pos_l(pos):
	return pos[0]

def pos_c(pos):
	return pos[1]

#Board

def board_size(board):
	return (len(board), len(board[0]))

def build_board_graph(board):
	size = board_size(board)
	graph = {}
	for l in range(0, size[0]):
		for c in range(0, size[1]):
			children = []
			if l > 0:
				children.append((l - 1, c))
			if c > 0:
				children.append((l, c - 1))
			if l < size[0] - 1:
				children.append((l + 1, c))			
			if c < size[1] - 1:
				children.append((l, c + 1))

			graph[(l, c)] = children
	return graph

def copy_board(board):
	copy = []
	size = board_size(board)
	for l in range(0, size[0]):
		line = []
		for c in range(0, size[1]):
			line.append(board[l][c])
		copy.append(line)
	return copy

def board_find_groups(board):
	copied_board = copy_board(board)
	size = board_size(board)
	board_graph = build_board_graph(board)
	groups = []
	for l in range(0, size[0]):
		for c in range(0, size[1]):
			if copied_board[l][c] != 0:
				groups.append(find_groups_aux(copied_board, board_graph, (l, c)))
	
	return groups
				
def find_groups_aux(board, graph, node):
	group = []
	parent_color = board[node[0]][node[1]]
	group.append(node)
	board[node[0]][node[1]] = 0
	for child in graph[node]:
		child_color = board[child[0]][child[1]]
		if child_color == parent_color and board[child[0]][child[1]] != 0:
			child_equal_nodes = find_groups_aux(board, graph, child)
			for g in child_equal_nodes:
				group.append(g)
	return group
					
def board_remove_group(board, group):
	size = board_size(board)
	copied_board = copy_board(board)
	for pos in group:
		copied_board[pos_l(pos)][pos_c(pos)] = 0				
		
	copied_board = vertical_crush(copied_board)
	copied_board = horizontal_crush(copied_board)

	return copied_board

def vertical_crush(board):
	size = board_size(board)
	for c in range(size[1]):
		first_empty = -1
		for l in range(size[0] - 1, -1, -1):
			if color(board[l][c]):
				board[first_empty][c],board[l][c] = board[l][c],board[first_empty][c]
				first_empty -= 1
	return board

def horizontal_crush(board):
	size = board_size(board)
	emptyColumns_Index = []
	notEmptyColumns_Index = []
	for c in range(0, size[1]):
		if color(board[-1][c]):
			notEmptyColumns_Index.append(c)
		else:
			emptyColumns_Index.append(c)
			
	rng = len(notEmptyColumns_Index)	
	for i in range(0, rng):
		for l in range(0, size[0]):
			board[l][i] = board[l][notEmptyColumns_Index[i]]
				
	for i in range(rng, rng + len(emptyColumns_Index)):
		for l in range(0, size[0]):
			board[l][i] = 0
	
	return board

board_remove_group([[1,1,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3]],[[0,0],[0,1]])
	
#SG_State

class sg_state():

	def __init__(self, b):
		self.board = b
	
	def __lt__(self, other_state):
		self.board<other_state.board

#Same Game

class same_game(Problem):

	def __init__(self, board):
		self.initial = sg_state(board)
		self.board = board

	def actions(self, state):
		groups = board_find_groups(state.board)
		actions = []
		for group in groups:
			if len(group) > 1:
				actions.append(group)
		return actions

	def result(self, state, action):
		if action in self.actions(state):
			return sg_state(board_remove_group(state.board, action))
		
	def goal_test(self, state):
		size = board_size(state.board)
		for l in range(0, size[0]):
			for c in range(0, size[1]):
				if state.board[l][c] != 0:
					return False
		return True		

	def path_cost(self, c, state1, action, state2):
		return c + 1

	def h(self, node):
		return len(board_find_groups(node.state.board))