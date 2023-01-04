from programs import brutessh
from programs import KeyboardRecord
from programs import porter
from programs import subs
from programs import maltego
from programs import IP
from programs import cracker
from programs import dirbuster
from programs import medusa
from programs import lynis
from programs import nmVul
from programs import nikto
from programs import aircrack
from programs import hashcat
from programs import john
from programs import pixiewps
from programs import reaver
from programs import kismet
from programs import wifite
from programs import netsniff
from programs import macchanger
from programs import powersploit
from programs import mimikatz
from programs import hydra
from programs import msfconsole
from programs import nmap
from programs import penner
from programs import set
#from programs import sqlmap
from programs import commix
from programs import wpscan
#from programs import skipfish
from programs import searchsploit
import os
import sys
from termcolor import colored
import time
import paramiko
import socket



def xxx():

	banner = '''


                       xxxxx                     xxxxx
                       xXXXXx                   xXXXXx
                        xXXXXx                 xXXXXx
                         xXXXXx               xXXXXx
                          xXXXXx             xXXXXx
                           xXXXXx           xXXXXx
                            xXXXXx         xXXXXx
                             xXXXXx       xXXXXx
                              xXXXXx     xXXXXx
 xxx             xxx           xXXXXx   xXXXXx             xxx             xxx
 xXXx           xXXx            xXXXXx xXXXXx              xXXx           xXXx
  xXXx         xXXx              xXXXXxXXXXx                xXXx         xXXx
   xXXx       xXXx                xXXXXXXXx                  xXXx       xXXx
    xXXx     xXXx                xXXXXxXXXXx                  xXXx     xXXx
     xXXx   xXXx                xXXXXx xXXXXx                  xXXx   xXXx
      xXXx xXXx                xXXXXx   xXXXXx                  xXXx xXXx             -Created-
       xXXxXXx                xXXXXx     xXXXXx                  xXXxXXx                -BY-
        xXXXx                xXXXXx       xXXXXx                  xXXXx              {hestihesti}
       xXXxXXx              xXXXXx         xXXXXx                xXXxXXx
      xXXx xXXx            xXXXXx           xXXXXx              xXXx xXXx
     xXXx   xXXx          xXXXXx             xXXXXx            xXXx   xXXx
    xXXx     xXXx        xXXXXx               xXXXXx          xXXx     xXXx
   xXXx       xXXx      xXXXXx                 xXXXXx        xXXx       xXXx
  xXXx         xXXx    xXXXXx                   xXXXXx      xXXx         xXXx
  xxx           xxx    xxxxx                     xxxxx      xxx           xxx


            xtract, xploit, xscape

	'''

	print(colored(banner, 'red'))
	catagory = '''

[i]nfo Gather
[v]ulnerability Analysis
[e]xploit
[p]assword Attacks
[w]ireless Attacks
[s]niffing and spoofing
[po]st-exploitation
[o]ther

[q]uit

'''

	apps1 = '''

[p]enner
[n]map
[g]obuster
[ip] address retriever
[m]altego
[s]ubdomainer
[po]rter

'''

	apps2 = '''

[nm]ap-sV
[n]map-scripts
[ni]kto
[l]ynis
[s]earchsploit

'''

	apps3 = '''

[m]edusa
[h]ashcat
[j]ohn
[hy]dra
[c]racker

'''

	apps4 = '''

[a]ircrack-ng
[p]ixiewps
[r]eaver
[w]ifite
[k]ismet

'''

	apps5 = '''

[m]acchanger
[n]etsniff-ng
[w]ireshark

'''

	apps6 = '''

[m]imikatz
[p]owersploit
[k]eylogger

'''

	apps7 = '''

[m]etasploit
[w]pscan
[s]qlmap
[c]ommix
[sf] skip-fish

'''

	apps8 = '''
[set] social-engineering-toolkit
[s]teggr
[b]ruteforce ssh

	'''

	option = ''
	while option != 'q':

		print(catagory)
		option = input('What Catagory Do You Want Go Into:\n> ')
		if option == 'i':
			print(apps1)
			run1 = input('Which Program Do You Want To Run:\n> ')
			if run1 == 'p':
				penner.pnr()
			elif run1 == 'n':
				nmap.nm()
			elif run1 == 'g':
				dirbuster.dir()
			elif run1 == 'ip':
				IP.grabber()
			elif run1 == 'm':
				maltego.mal()
			elif run1 == 's':
				subs.doms()
			elif run1 == 'po':
				porter.sCAN()
			else:
				print('Invalid Input')

		elif option == 'v':
			print(apps2)
			run2 = input('Which Program Do You Want To Run:\n> ')
			if run2 == 'n':
				nmVul.vulner()
			elif run2 == 'nm':
				nmap.nm()
			elif run2 == 'ni':
				nikto.NIK()
			elif run2 == 'l':
				lynis.lyn()
			elif run2 == 's':
				searchsploit.search()
			else:
				print('Invalid Input')

		elif option == 'p':
			print(apps3)
			run3 = input('Which Program Do You Want To Run:\n> ')
			if run3 == 'm':
				medusa.medsa()
			elif run3 == 'j':
				john.theRipper()
			elif run3 == 'h':
				hashcat.hc()
			elif run3 == 'hy':
				hydra.dra()
			elif run3 == 'c':
				cracker.crk()
			else:
				print('Invalid Input')

		elif option == 'w':
			print(apps4)
			run4 = input('Which Program Do You Want To Run:\n> ')
			if run4 == 'a':
				aircrack.ac()
			elif run4 == 'w':
				wifite.fite()
			elif run4 == 'k':
				kismet.ksmt()
			elif run4 == 'p':
				pixiewps.pixie()
			elif run4 == 'r':
				reaver.reav()
			else:
				print('Invalid Input')

		elif option == 's':
			print(apps5)
			run5 = input('Which Program Do You Want To Run:\n> ')
			if run5 == 'm':
				macchanger.change()
			elif run5 == 'n':
				netsniff.nets()
			elif run5 == 'w':
				wiresrk = 'wireshark'
				os.system(wiresrk)
			else:
				print('Invalid Input')

		elif option == 'po':
			print(apps6)
			run6 = input('Which Program Do You Want To Run:\n> ')
			if run6 == 'm':
				mimikatz.katz()
			elif run6 == 'k':
				KeyboardRecord.rec()
			elif run6 == 'p':
				powersploit.power()

			else:
				print('Invalid Input')

		elif option == 'e':
			print(apps7)
			run7 = input('Which Program Do You Want To Run:\n> ')
			if run7 == 'm':
				msfconsole.msf()
			elif run7 == 'c':
				commix.com()
			elif run7 == 's':
				sqlmap.map()
			elif run7 == 'w':
				wpscan.scan()
			elif run7 == 'sf':
				skipfish.fish()

			else:
				print('Invalid Input')

#		import set
		elif option == 'o':
			print(apps8)
			run8 = input('Which Program Do You Want To Run:\n> ')
			if run8 == 'set':
				set.toolkit()
			elif run8 == 's':
				steggr.steg()
			elif run8 == 'b':
				brutessh.bruter()



		elif option == 'q':
			c = 'clear'
			os.system(c)
			break

		else:
			print('Invalid Input')

xxx()
