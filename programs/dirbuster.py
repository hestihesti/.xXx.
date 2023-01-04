import os
import sys
from termcolor import colored
import time


def dir():
	site = input('What Site Would Like To Scan For Their Directories:\n> ')
	wl = '/usr/share/dirbuster/wordlists/directory-list-1.0.txt'
	gobuster = 'gobuster -u ' + site + ' -w ' + sl + ' dir'
	gt = 'gnome-terminal -x ' + gobuster
	os.system(gt)
