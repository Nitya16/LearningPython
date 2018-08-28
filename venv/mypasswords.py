#! python3

# CLI tool for retreiving passwords to accounts
import sys, pyperclip

PASSWORDS = {'email1': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'email2': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'email3': '12345'}
print("Hello Nitya")
print(sys.argv)
if len(sys.argv) != 2 :
    print('Usage: python mypasswords.py [yourAccountName]')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

