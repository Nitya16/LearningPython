#! python3

# CLI tool for retreiving passwords to accounts
import sys, pyperclip, getpass


PASSWORDS = {'email1': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'email2': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'email3': '12345'}
print("Hello Nitya")
mainpass= getpass.getpass('Enter the Password:')
print(sys.argv)

if mainpass != 'nityagovind':
    print('Wrong Password')

while(mainpass== 'nityagovind'):

    if len(sys.argv) != 2 :
        print('Usage: python mypasswords.py [yourAccountName]')
        sys.exit()

    account = sys.argv[1]      # first command line arg is the account name

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
        break
    else:
        print('There is no account named ' + account)
        break