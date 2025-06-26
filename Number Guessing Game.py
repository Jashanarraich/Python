import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    attempts = 10
    if difficulty == "hard":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
        return attempts
    elif difficulty == "easy":
        print(f"You have {attempts} attempts remaining to guess the number.")
        return attempts
    return None


def game():
    game_over = False
    number = random.randint(1, 100)
    chances = set_difficulty()
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_over = True

        elif guess > number:
            print("Too High! Try again. ")
            chances -= 1

        elif guess < number:
            print("Too Low! Try again")
            chances -= 1

        if chances == 0:
            game_over = True
            print(f"You are out of attempts the number was {number}")
        if chances > 0:
            print(f"You have {chances} attempts remaining.")
game()
