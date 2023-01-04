import sys
import os
from termcolor import colored


def map():
	url = input('What Is The Website URL:\n> ')
	sqlmap = 'sqlmap -u ' + url + ' --wizard'
	gt = 'gnome-terminal -x ' + sqlmap
	os.system(gt)
