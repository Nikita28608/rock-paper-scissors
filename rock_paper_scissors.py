import random
'''
rock=1
paper=0
scissors=-1
'''
computer=random.choice([-1,0,1])
yourchoice=input("enter the your choice ")
youdict={"r":1,"p":0,"s":-1}
reversedict={1:"rock",0:"paper",-1:"scissors"}
you=youdict[yourchoice]
print(f"Computer choice is {reversedict[computer]} and your choice is {reversedict[you]}")

if computer==you:
    print("It's a draw")
else:
    if computer==0 and you==1:
       print("You Lose!")
    elif computer==0 and you==-1:
       print("You Win!")
    elif computer==1 and you==0:
       print("You Win!")
    elif computer==1 and you==-1:
       print("You lose!")
    elif computer==-1 and you==1:
       print("You Win!")
    elif computer==-1 and you==0:
       print("You lose!")
    else:
       print("somthing went wrong")
 