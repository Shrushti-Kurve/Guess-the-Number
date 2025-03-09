import random

target = random.randint(1,100)

while True:
    userchoice = int(input("enter the number"))
    if(userchoice == target):
        print("yeahh : correct guess")
        break
    if(userchoice < target):
        print("number is small ")
    else:
        print("your no is big")
print("Game Over")