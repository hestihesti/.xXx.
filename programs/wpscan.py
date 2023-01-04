import os
import sys
from termcolor import colored


def scan():
	url = input('What Is The URL:\n> ')
	filename = input('Output File Name (include ext.. .txt. md):\n> ')
	pswords = input('Provide/Path/To/Password/Wordlist.txt:\n> ')
	user = input('Provide/Path/To/Usernames/Wordlist.txt:\n> ')
	attack = '''

SELECT A PASSWORD ATTACK

[wp-login]
[xmlrpc]
[xmlrpc-multicall]

'''
	print(attack)
	atk = input('> ')
	wps = 'wpscan -v --url ' + url + ' -o ' + filename + ' --random-user-agent -e ap -P ' + pswords + ' -U ' + user + ' --password-attack ' + atk + ' --stealthy'
	gt = 'gnome-terminal -x ' + wps
	os.system(gt)
