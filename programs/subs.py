import requests
import sys

def doms():
	s = str(input('Provide A Subdomains List With ".txt":\n> '))
	sublist = open(s).read()
	subdoms = sublist.splitlines()

	for sub in subdoms:
		sub_domains = f'http://{sub}.{sys.argv[1]}'

		try:
			requests.get(sub_domains)
		except:
			pass
		else:
			print('Valid domain: '.sub_domains)
