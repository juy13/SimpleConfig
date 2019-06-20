import os
import sys

import ply.lex as lex
from ply.lex import TOKEN
import re

debug = True
line_pos = 0
pos = 0

def log(came_log):
	if debug:
		print(came_log)
	if not debug:
		return 0

reserved = {
	 'LENGTH' 		: 'length',
	 'HEIGTH' 		: 'heigth',
	 'COLOR'		: 'color',
	 'NAME'			: 'name',
	 'VERSION'		: 'version'
	}

tokens = ['NAMES', 'COMMENT', 'EQ', 'VER', 'COL', 'SIZE'] + list(reserved.values())

t_NAMES = r'\".*?\"'
t_COMMENT = r'\;.*'
t_EQ = r'='
t_VER = r'[0-9]+.[0-9]+.[0-9]+([a,b]?)'
t_COL = r'[#][0-9a-f]{6}'
t_SIZE = r'[1-9][0-9]{0,8}'

t_ignore = ' \r\t\f\n'

def t_newline(t):
	r'\n'
	#log('HERE')
	global line_pos
	t.lexer.lineno += 1
	line_pos += 1
	log('LINE: ' + str(line_pos))

def t_error(t):
	return print("Illegal character '%s' at line '%s'" % (t.value[0], t.lexer.lineno))	 

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t

if __name__ == '__main__':
	file = open('config.cfg', 'r')
	lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)
	
	for line in file:
		lexer.input(line)
		while True:
					tok = lexer.token() # читаем следующий токен
					if not tok: break	# закончились печеньки		
					log (tok)
