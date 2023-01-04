import os
import sys
from termcolor import colored
import time


def change():
	int = input('What Interface Do You Want To Change It On:\n> ')
	o = '''
[r]andom mac
[p]retend to be a burned-in-mac
	'''
	print(colored(o, 'yellow'))
	if o == 'r':
		mac = 'macchanger -r ' + int
		os.system(mac)
	elif o == 'p':
		mac2 = 'macchanger -b ' + int
		os.system(mac2)
	else:
		print('Invalid Input')
