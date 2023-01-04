import os
import sys
from termcolor import colored


def pnr():

#	nmap = 'nmap -v -sS -p21 -D RND:5 ') + 

	try:
		with open('IPs.txt', 'r') as r:
			lines = r.readlines()
			port = input('What Port Are You Trying To Scan:\n> ')
			for line in lines:
#				port = input('What Port You Trying To Scan:\n> ')
				nmap = f'nmap -v -sS -p{port} -D RND:5 {line}/24'
#				gt = 'gnome-terminal -x ' + nmap
				os.system(nmap)
	except:
		print('Something Went Wrong')


