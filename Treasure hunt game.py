print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____''')

print("Welcome to the Treasure island.\nYour mission is to find the treasure.\n")
turn = input("You're at a cross road. Where do you want to go?\nType left or right \n")
if turn == "Right" or turn == "right":
    print("You fell into a hole.Game Over!\n")

elif turn == "Left" or turn == "left":
        print("You've come to a lake. There is an island in the middle of the lake.\n")
        swim = input("Type wait to wait for a boat. Type swim to swim across.\n")
        if swim == "swim" or swim == "Swim":
            print("You got attacked by an angry trout. Game Over.\n")
        elif swim == "wait" or swim == "Wait":
            color = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n")
    
            if color == "Red" or color == "red":
                print("It's a room full of fire. Game Over.\n")
            elif color == "Blue" or color == "blue":
                print("You enter a room of beasts. Game Over.\n")
            elif color == "Yellow" or color == "yellow":
                print("You found the treasure! You Win!\n")
            else:
                print("Invalid inputs!\n")
        else:
            print("Invalid inputs!\n")

else:
    print("Invalid inputs!\n")
