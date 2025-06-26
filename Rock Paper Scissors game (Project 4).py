import random

choices = ["rock", "paper", "scissor\n"]
user_choice = input("What do you choose?Rock, Paper, Scissor\n").lower()
com_choice = random.choice(choices)
print(f"You chose {user_choice}\n")
print(f"Computer chose {com_choice}\n")
if user_choice == com_choice:
    print("Match Draw\n")
elif user_choice == "rock" and com_choice == "paper":
    print("You Lost\n")
elif user_choice == "rock" and com_choice == "scissor":
    print("You Won\n")
elif user_choice == "paper" and com_choice == "rock":
    print("You Won")
elif user_choice == "paper" and com_choice == "scissor":
    print("You Lost\n")
elif user_choice == "scissor" and com_choice == "rock":
    print("You Lost")
elif user_choice == "scissor" and com_choice == "paper":
    print("You Won\n")
else:
    print("Invalid input\n")