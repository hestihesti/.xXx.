import os
import sys
from termcolor import colored

def hc():
	successful = input('Name File That Will Store All Cracked Hashes:\n> ')
	dict = input('File That Holds A Dictionary Of Known Hashes:\n> ')
	wl = input('Provide A Wordlist You Would Like T Use:\n> ')


	hash = 'hashcat -m 500 -a 0 ' + successful + ' ' + dict + ' ' + wl
	gt = 'gnome-terminal ' + hash
	os.system(gt)
