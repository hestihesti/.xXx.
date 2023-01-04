import os
import sys
from termcolor import colored
import time

def vulner():
	with open('IPs.txt', 'r') as r:
		lines = r.readlines()
		for line in lines:
#	target = input('What Is Your Targets IP:\n> ')
			ana = f'nmap -v --script auth {line} -sS -d'
			ana2 = f'nmap -v --script banner {line} -sS -d'
			ana3 = f'nmap -v --script vuln {line} -sS -d'
			ana4 = f'nmap -v --script exploit {line} -sS -d'
			'''
	term1 = 'gnome-terminal ' + ana
	term2 = 'gnome-terminal ' + ana2
	term3 = 'gnome-terminal ' + ana3
	term4 = 'gnome-terminal ' + ana4
			'''

			print(colored('Please Be Patient While Program Runs', 'red'))
			time.sleep(2)
			os.system(ana)
			os.system(ana2)
			os.system(ana3)
			os.system(ana4)
