import random

player1 = input("enter player 1 name")
player2 = input("enter player 2 name")

RdmNumber = random.randint(1, 10000)
Userguess = 0

print("Who will find the number at first")
print("the number is between 1 and 10 000")

while Userguess != RdmNumber:
    print("it's " + player1 + " turn")
    Userguess = int(input(player1 + " please enter a guess"))
    if Userguess == RdmNumber:
        break
    elif Userguess > RdmNumber:
        print("The number to find is smaller")
    elif Userguess < RdmNumber:
        print("The number to find is bigger")
        
    Userguess = int(input(player2 + " please enter a guess"))
    if Userguess > RdmNumber:
        print("The number to find is smaller")
    elif Userguess < RdmNumber:
        print("The number to find is bigger")

print("You won, number was indeed " + str(RdmNumber))
