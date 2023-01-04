import os
import sys
from termcolor import colored
import time


def msf():
	db = input('Do You Currently Have A Working Database With Metasploit <y/n>:\n> ')
	if db == 'y':
		serv = 'systemctl postgresql start'
		os.system(serv)
		con = 'msfconsole'
		gt = 'gnome-terminal -x ' + con
		os.system(gt)

	elif db == 'n':
		ini = 'msfdb init'
		serv = 'systemctl postgresql start'
		os.system(ini)
		os.system(serv)
		console = 'msfconsole'
		gt = 'gnome-terminal -x ' + console
		os.system(gt)

	else:
		print('Invalid Input')
