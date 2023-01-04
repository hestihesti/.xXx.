import os
import sys
from termcolor import colored



def medsa():
	try:
		file = input('What Is Your Targets IP:\n> ')
		user = input('Provide A .TXT List Of Usernames:\n> ')
		pwd = input('Provide A .TXT List Of Passwords:\n> ')
		modules = '''
[cvs]
[ftp]
[http]
[imap]
[mssql]
[mysql]
[nntp]
[pcanywhere]
[pop3]
[postgres]
[rexec]
[rlogin]
[rsh]
[smbnt]
[smtp]
[sntp]
[ssh]
[svn]
[telnet]
[vnc]
[web-form]
[wrapper]

		with open(file, 'r') as r:
			lines = r.readlines()
			for line in lines:
		'''
		print(colored(modules, 'magenta'))
		mod = input('What Module Would You Like To Use:\n> ')
		port = input('What Port Number Is That Module On:\n> ')
#		with open(file, 'r') as r:
#			lines = r.readlines()
#			for line in lines:
		dusa = 'medusa -h ' + file + ' -u ' + user + ' -P ' + pwd + ' -M ' + mod + ' -n ' + port
		gt = 'gnome-terminal -x ' + dusa
		os.system(gt)
	except:
		print('Something Wrong Happened')

