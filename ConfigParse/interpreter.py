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
		self._Color = []
		self._Name = ''
		self._Version = [0, 0, 0, '']
		self._Comments = []

	def conf(self, data):
		for sentence in data:
			if sentence[0] == 'Comment':
				self._Comments.append(sentence[1])
			if sentence[0] == 'Length':
				self._Length += int(sentence[1])
			if sentence[0] == 'Heigth':
				self._Heigth += int(sentence[1])
			if sentence[0] == 'Color':
				self._Color = self._fromStrToByte(sentence[1][1:])
			if sentence[0] == 'Name':
				self._Name += sentence[1]
			if sentence[0] == 'Version':
				self._Version[0] = int(sentence[1][0])
				self._Version[1] = int(sentence[1][2])
				self._Version[2] = int(sentence[1][4])
				if len(sentence[1]) == 6:
					self._Version[3] += sentence[1][5]
			print(sentence)

	def _fromStrToByte(self, came_str):
		flag = False
		bt = [0x00, 0x00, 0x00]
		b = 0
		c = 0
		buf = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		j = 0
		for i in came_str:
			if i in buf:
				b = int(i)
			else:
				if i == 'a':
					b = 10
				if i == 'b':
					b = 11
				if i == 'c':
					b = 12
				if i == 'd':
					b = 13
				if i == 'e':
					b = 14
				if i == 'f':
					b = 15
			if flag == False:
				c = b << 4
				flag = True
				continue
			if flag == True:
				c = c | b
				bt[j] = c
				j += 1
				c = 0
				b = 0
				flag = False

		return bt
		



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
	lst = parser_cfg.lst
	A = ConfigStruct()
	A.conf(lst)
	
	