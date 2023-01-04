import pyfiglet
import hashlib
from termcolor import colored

def crk():
	ascii_banner = pyfiglet.figlet_format('Hash\n Cracker')
	print(ascii_banner)

	def tryOpen(wordlist):
		global pass_file
		try:
			pass_file = open (wordlist, "r")
		except:
			print("[!!] No File Under That Name Exists In The Path!")
			quit()

	pass_hash = input("[*] Enter MD5 Hash Value: ")

	q = input('Name Of Wordlist (** include extension **):  ')
	wl = '/home/d0c0b/Packages/Wordlist/' + q
	wordlist = wl
	tryOpen(wordlist)

	for word in pass_file:
		print(colored("[-] Trying: " + word.strip("\n"), 'red'))
		enc_wrd = word.encode('utf-8')
		md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

		if md5digest == pass_hash:
			print(colored("[+] Password Found: " + word, 'green'))
			exit(0)

	print(colored("[-] Password Not In List", 'yellow'))
