import os
import sys
from termcolor import colored


def lyn():
	select = '''
[s]can local computer
[r]emote scan
	'''
	print(select)
	opt = input('> ')
	if opt == 's':
		l = 'lynis audit system'
		os.system(l)

	elif opt == 'r':
		target = input('What Is Your Targets IP Address:\n> ')
		lr = 'lynis audit system remote' + target
		os.system(lr)

	else:
		print('Invalid Input')
