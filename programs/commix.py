import os
import sys
from termcolor import colored


def com():
	'''
#	q1 = input('Would You Like To Scan A [s]ingle Target OR [m]ultiple targets')
	web = input('What Is The Websites URL:\n> ')
	post = input('Put In Your POST Data Here:\n> ')
	crawl = input('What Crawl Depth Would You Like To Implement:\n> ')
	'''
	web = input('What Is The Website URL:\n> ')
	commix = 'commix -u ' + web + ' --wizard'
	gt = 'gnome-terminal -x ' + commix
	os.system(gt)
