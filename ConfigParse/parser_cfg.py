import ply.lex  as lex
import ply.yacc as yacc
import pickle

import tokins
#handle = open('res.cfg', 'w')

debug = True
def log(came_log):
	if debug:
		with open('res.cfg', 'a') as handle:
				handle.write(str(came_log) + '\n')
	if not debug:
		return 0

tokens = tokins.tokens

lst = []

def p_program(p):
	'''program : sentences'''
	p[0] = {}
	if 0 not in p[0]:
		p[0][0] = [p[1][1]]
	else:
		p[0][0].append(p[1][1])

#def p_statement(p):
#	'''statement : sentences'''
#	p[0] = (p[1])
	
def p_sentences(p):
	'''sentences : sentence sentences
				 | sentence'''
	if len(p) == 3:
		p[0] = (p[1], p[2])
	else:
		p[0] = [p[1]]

def p_sentence(p):
	'''sentence : Length
				| Heigth
				| Color
				| Name
				| Version
				| Comment'''
	log(p[1])
	p[0] = (p[1])
	log(p[0])

def p_comment(p):
	'''Comment : COMMENT'''
	p[0] = ('Comment', p[1])
	lst.append(p[0])

def p_length(p):
	'''Length : length EQ SIZE'''
	p[0] = ('Length', p[3])
	lst.append(p[0])

def p_heigth(p):
	'''Heigth : heigth EQ SIZE'''
	p[0] = ('Heigth', p[3])
	lst.append(p[0])

def p_color(p):
	'''Color : color EQ COL'''
	p[0] = ('Color', p[3])
	lst.append(p[0])

def p_name(p):
	'''Name : name EQ NAMES'''
	p[0] = ('Name', p[3])
	lst.append(p[0])

def p_version(p):
	'''Version : version EQ VER'''
	p[0] = ('Version', p[3])
	lst.append(p[0])

def p_error(p):
	pass

parser = yacc.yacc(debug=0, write_tables=0)	
	
def parse(data, debug=0):
	parser.error = 0
	parser.lineno = 1
	try:
		p = parser.parse(data, debug=debug)
	except lex.LexError:
		p = None
	return p



if __name__ == '__main__':

	def lexx(lexer, data):
		lexer.input(data)
		while True:
			tok = lexer.token()
			if not tok:
				break
			log(tok)
		lexer.lineno = 1
				
	lexer = lex.lex(module=tokins)
	#dex2r_lex.log()
	data = open('config.cfg').read()
	lexx(lexer, data)
	#dex2r_lex.log()
	prog = parse(data, 1)
	print(prog)
	print(lst)