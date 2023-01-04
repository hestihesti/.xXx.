import os
import sys
from termcolor import colored
import time


def nets():
	pcap = input('Name The PCAP File:\n> ')
	inter = input('Enter The Network Interface You Want To Spy On:\n> ')
	sniff = 'netsniff-ng --in ' + inter + ' --out ' + pcap + '.pcap --silent --bind-cpu 0'
	gt = 'gnome-terminal ' + sniff
	os.system(gt)
