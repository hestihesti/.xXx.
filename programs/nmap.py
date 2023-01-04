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
			nmap2 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q2 + ' -oX ' + q2 + '.xml'
			gnome = 'gnome-terminal -x ' + nmap1
			gnome2 = 'gnome-terminal -x ' + nmap2
			os.system(gnome)
			os.system(gnome2)
			print(colored('Results Were Saved As.. ' + q2 + '.xml', 'green'))
		elif ques == 'y':
			nmap1 = 'nmap -v -O -D RND:5 ' + q2 + '/24'
			nmap2 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q2 + '/24 -oX ' + q2 + '.xml'
			gnome = 'gnome-terminal -x ' + nmap1
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
			nmap4 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q4 + ' -oX ' + q4 + '.xml'
			gnome3 = 'gnome-terminal -x ' + nmap3
			gnome4 = 'gnome-terminal -x ' + nmap4
			os.system(gnome3)
			os.system(gnome4)
			print(colored('Results Were Saved As.. ' + q4 + '.xml', 'green'))
		elif ques == 'y':
			nmap3 = 'nmap -v -O -D RND:5 ' + q4 + '/24'
			nmap4 = 'nmap -v -sV --version-intensity 9 -D RND:7 -p7,19,20,21,22,23,25,37,53,69,79,80,110,111,135,137,138,139,445,161,443,512,513,514,1433,1434,1723,3389,8080 ' + q4 + '/24 -oX ' + q4 + '.xml'
			gnome3 = 'gnome-terminal -x ' + nmap3
			gnome4 = 'gnome-terminal -x ' + nmap4
			os.system(gnome3)
			os.system(gnome4)
			print(colored('Results Were Saved As.. ' + q4 + '.xml', 'green'))

		else:
			print('Invalid Input')



	else:
		print(colored('Invalid Input', 'red'))
