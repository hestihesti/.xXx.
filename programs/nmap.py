import os
import sys
from termcolor import colored

def nm():
	q1 = input('[ip] Address Or [web]site:  ')
	if q1 == 'ip':
		q2 = input('Type In The IP Address You Would Like To Scan: ')
		ques = input('Would You Like To Check Devices Connected To This IP Address <y/n>:\n> ')
		if ques == 'n':
			nmap1 = 'nmap -v -O -D RND:5 ' + q2
			nmap2 = 'nmap -O -Pn -sV -p- ' + q2 ' --max-rtt-timeout=3000ms --min-rtt-timeout=500ms --defeat-rst-ratelimit --max-retries=3 --scan-delay 50ms --max-rate 3 --top-ports 1000 --version-intensity 5 -o ' + q2 + '.md'
			gnome = 'gnome-terminal -x ' + nmap1
			gnome2 = 'gnome-terminal -x ' + nmap2
#			os.system(gnome)
			os.system(gnome2)
			print(colored('Results Were Saved As.. ' + q2 + '.xml', 'green'))
		elif ques == 'y':
			nmap1 = 'nmap -v -O -D RND:5 ' + q2 + '/24'
			nmap2 = 'nmap -O -Pn -sV -p- ' + q2 '/24 --max-rtt-timeout=3000ms --min-rtt-timeout=500ms --defeat-rst-ratelimit --max-retries=3 --scan-delay 50ms --max-rate 3 --top-ports 1000 --version-intensity 5 -o ' + q2 + '.md'
#			gnome = 'gnome-terminal -x ' + nmap1
			gnome2 = 'gnome-terminal -x ' + nmap2
			os.system(gnome)
			os.system(gnome2)
			print(colored('Results Were Saved As.. ' + q2 + '.xml', 'green'))
		else:
			print('Invalid Input')

	elif q1 == 'web':
		q4 = input('What Is The Website URL: ')
		ques = input('Would You Like To Check The Devices Connected To Their Network:\n> ')
		if ques == 'n':
			nmap3 = 'nmap -v -O -D RND:5 ' + q4
			nmap4 = 'nmap -O -Pn -sV -p- ' + q2 ' --max-rtt-timeout=3000ms --min-rtt-timeout=500ms --defeat-rst-ratelimit --max-retries=3 --scan-delay 50ms --max-rate 3 --top-ports 1000 --version-intensity 5 -o ' + q2 + '.md'
			gnome3 = 'gnome-terminal -x ' + nmap3
			gnome4 = 'gnome-terminal -x ' + nmap4
#			os.system(gnome3)
			os.system(gnome4)
			print(colored('Results Were Saved As.. ' + q4 + '.xml', 'green'))
		elif ques == 'y':
			nmap3 = 'nmap -v -O -D RND:5 ' + q4 + '/24'
			nmap4 = 'nmap -Pn -sV -p- ' + q4 '/24 --max-rtt-timeout=3000ms --min-rtt-timeout=500ms --defeat-rst-ratelimit --max-retries=3 --scan-delay 50ms --max-rate 3 --top-ports 1000 --version-intensity 5 -o ' + q2 + '.md'
			gnome3 = 'gnome-terminal -x ' + nmap3
			gnome4 = 'gnome-terminal -x ' + nmap4
			os.system(gnome3)
#			os.system(gnome4)
			print(colored('Results Were Saved As.. ' + q4 + '.xml', 'green'))

		else:
			print('Invalid Input')



	else:
		print(colored('Invalid Input', 'red'))
