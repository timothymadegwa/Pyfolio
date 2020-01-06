import random
import time
print('Welcome to the Rolling dice!')
print('- - - '*10)
ans='Y'

def roll_the_dice(ans):
    if type(ans)!= str:
        raise TypeError('You have entered a wrong value. Kindly enter Y/N')
    ans=ans.upper()
    if ans=='Y':
        print('Rolling.....\n')
        time.sleep(3)
        dice=random.randint(1,6)
        print('You rolled a ',dice)
    elif ans=='N':
        print('Thanks for playing. See you next time')
    else:
        print('you have entered a wrong value. Kindly enter Y/N')
    return ans
    

while ans!="N":
    ans=input('Do you want to roll the dice?  (Y/N)\n')
    ans=roll_the_dice(ans)

