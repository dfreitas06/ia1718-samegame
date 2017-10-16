#Same Game
#IA 17/18
#
#Author: Diogo Freitas   ist181586
#Author: Joao Rodrigues  ist424786

from search.py import * 
from utils.py import * 

#Provided Boards

board1 = [[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]]															#4x5 board with 2 colors, no solution
board2 = [[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]															#4x5 board with 3 colors
board3 = [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[5,1,1,3],[4,5,1,2]]		#10x4 board with 3 colors, no solution
board4 = [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]		#10x4 board with 3 colors
board5 = [[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]		#10x4 board with 5 colors

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

#Group


#Board

def board_size(board):
	return (len(board), len(board[0]))

def board_find_groups(board):
	for l in range (0, size[0]):
		for c in range (0, size[1]):
			pos = (l, c)	

				
	return null

def board_find_groups_aux(board, groups, currGroup, pos):
	size = board_size(board)

	pos_checked_flag = False
	for x in range (0, len(groups)):
		if pos in groups[x]:
			pos_checked_flag = True
		
		if pos_checked_flag == False:
			group = [pos]
			group = group + board_find_groups_aux(board
	return groups
	

def board_remove_group(board, group):
	return null

#SG_State

#Same Game

class same_game(Problem):

	def _init_(self, board):
		return null

	def actions(self, state):
		return null

	def result(self, state, action):
		return null

	def goal_test(self state):
		return null

	def path_cost(self, c, state1, action, state2):
		return null

	def h(self, node):
		return null