import os
import sys
from termcolor import colored
import time



def theRipper():
	optn = '''

[c]rack hashes
[l]isten to interface on network for logins and saved discoveries
[b]itlocker cracker
[k]eepass cracker
[r]ar cracker
[z]ip folder cracker
[w]pcap2john converts pcap files into a johntheripper format

'''
	print(optn)
	ui = input('What Action Are You Trying To Perform:\n> ')
	if ui == 'c':
		wl = input('Provide Path To Wordlist:\n> ')
		hashes = input('What Is Your Name Of The File That Storing Your Hashes(include .txt):\n> ')
		j1 = 'john --wordlist=' + wl + ' --rules ' + hashes
		gnome = 'gnome-terminal ' + j1
		os.system(gnome)

	elif ui == 'l':
		inter = input('Name Of Interface:\n> ')
		dumpfile = input('Name Of Dump File:\n> ')
		sipd = 'sipdump -i ' + inter + ' ' + dumpfile
		gt = 'gnome-terminal ' + sipd
		os.system(gt)

	elif ui == 'b':
		image = input('What Is The Name Of The Encrypted Image:\n> ')
		bit = 'bitlocker2john -i ' + image
		gnme = 'gnome-terminal ' + bit
		os.system(gnme)

	elif ui == 'k':
		key = input('Name Of The Key File:\n> ')
		database = input('Name Of The .kdbx Database:\n> ')
		kp2j = 'keepass2john -k ' + key + ' ' + database
		gt = 'gnome-terminal ' + kp2j
		os.system(gt)

	elif ui == 'r':
		name = input('Name Of The RAR File:\n> ')
		r2j = 'rar2john -v ' + name
		gt = 'gnome-terminal ' + r2j
		os.system(gt)

	elif ui == 'z':
		name = input('Name Of The Locked Zip Folder:\n> ')
		z2j = 'zip2john -a ' + name
		gt = 'gnome-terminal ' + z2j
		os.system(gt)

	elif ui == 'w':
		essidMAC = input('What Is The ESSID and MAC (put it in this format "ESSID:MAC_ADDRESS":\n> ')
		pcap = input('What Is The Name Of The PCAP File:\n> ')
		wp2j = 'wpapcap2john -c -e ' + essidMAC + ' ' + pcap
		gt = 'gnome-terminal ' + wp2j
		os.system(gt)

	else:
		print('Invalid Input')
