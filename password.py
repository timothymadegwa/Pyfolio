import string
import time
import getpass
print('Please enter your password followed by the enter key.')  
psw=getpass.getpass()
err=0
def password_validator(psw): 
    err=0
    l=len(psw)
    print('Validating your password.....\n')
    if l>12:
        print('Password too long')
        time.sleep(1)
        err=err+1
    elif l<6:
        print('Password too short')
        time.sleep(1)
        err=err+1
    else:
        print('Password length is OK')
    if any(low.islower() for low in psw):
        print('Lowercase letter detected')
        time.sleep(1)
    else:
        print('Your password needs a lowercase letter')
        err=err+1
        time.sleep(1)
    if any(upper.isupper() for upper in psw):
        print('Uppercase letter detected')
        time.sleep(1)
    else:
        print('Your password needs an uppercase letter')
        err=err+1
        time.sleep(1)
    if any(digit.isdigit() for digit in psw):
        print('digit detected')
        time.sleep(1)
    else:
        print('Your password needs a digit')
        err=err+1
        time.sleep(1)
    special_char=string.punctuation
    if any(a in special_char for a in psw):
        print('Special character detected')
        time.sleep(1)
    else:
        print('Your password needs a special character')
        err=err+1
        time.sleep(1)
    if err>0:
        print("The password is invalid. It has",err,'error(s).\nKindly correct them')
    else:
        print('Your password is Valid. You are good to go!')
password_validator(psw)