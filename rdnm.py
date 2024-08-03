import random

target = random.randint(1, 100)

while True:
    user_Choice = int(input("Guess the number between 1 and 100 :"))
    if (user_Choice == target):
        print("You guess it right")
        print(target)
        
        break
    elif(user_Choice > target):
        print("Your Choice is too large, take a smaller guess ")
    else:
        print("Your Choice is too small, take a larger guess ")


print("_____gameover____")