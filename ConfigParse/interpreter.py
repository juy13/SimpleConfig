import os 
import sys
import ply.lex  as lex
import ply.yacc as yacc
import tokins
import parser_cfg

debug = True
def log(came_log):
	if debug:
		print(came_log)
	if not debug:
		return 0


class ConfigStruct:
	
	def __init__(self):
		self._Length = 0
		self._Heigth = 0
		self._Color = {0x00, 0x00, 0x00}
		self._Name = ''
		self._Version = {0, 0, 0}

	def conf(self, data):
		for sentence in data:
			print(sentence)



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

	prog = parser_cfg.parse(data, 1)

	A = ConfigStruct()
	A.conf(prog)
	
	