#simple version of program password lock
PASSWORDS = {'email':'passoword_1',
	         'website':'password_2',
			 'fb':'password_3'
	         }
import sys,pyperclip
if len(sys.argv)<2:
	print('Usage: py pw.py [account] - copy account password')
	sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Your "+ account +" password is copied to clipboard")
else:
	print("Your "+ account+" not found")
	
	
