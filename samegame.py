#Same Game
#IA 17/18
#
#Author: Diogo Freitas   ist181586
#Author: Joao Rodrigues  ist424786

import * from search.py
import * from utils.py

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

def board_find_groups(board):
	return null

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