print("=============== Guess Number ===============")
print("Welcome to the game, pro.")

print("The computer choose random number, and you try to find this number.")
print("Random number between 1 , 100")

import random
number_by_com = random.randint(1,100)
count = 0

user = input("You ready to play (yes , No) ? ").strip().lower()

if user == "yes" or user == "y" or user == "ye" :

    while True:
        num = int(input("Enter Guess number : "))
        if number_by_com == num :
            print("You Guess corect. Nice")
            break
        elif number_by_com > num :
            print("The random number is greater than number you choosen.")
            count += 1
        elif number_by_com < num :
            print("The random number is smaller than number you choosen.")
            count += 1

    print(f"Your Guess correct the random num {num}, Your tries {count} wrong.")

else :
    print("No problem, Play in anther time.")

