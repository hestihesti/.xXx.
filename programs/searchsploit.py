import os
import sys
from termcolor import colored


def search():
	i = ''
	while i != 'q':
		print(colored('Press "q" To Quit', 'red'))
		i = input('What Version Are You Looking Into:\n> ')
		ss = 'searchsploit ' + i
		os.system(ss)
