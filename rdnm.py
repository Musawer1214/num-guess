import random

target = random.randint(1, 100)

while True:
    #First we will check if he want to continue the game or quit the game
    user_Choice = input("Guess a number or press q to quit the game :")
    if (user_Choice == "q"):
        break

    user_Choice = int(user_Choice)
    #In the above line we will convert the inout into an Integer to compare it with the guess number
    if (user_Choice == target):
        print("Congrats! You guess it right")
        print(target)
        break
    
    elif(user_Choice > target):
        print("Your Choice is too large, take a smaller guess ")
    else:
        print("Your Choice is too small, take a larger guess ")


print("_____gameover____")