import os
import sys
from termcolor import colored


def ksmt():
	card = 'airmon-ng start wlan0'
	kmt = 'kismet -c wlan0mon'
	gt = 'gnome-terminal ' + kmt
	os.system(gt)

