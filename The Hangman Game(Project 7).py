import random
stages = [r''' +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()

word_list = [
    "python", "keyboard", "program", "developer", "function",
    "variable", "loop", "string", "integer", "condition",
    "hangman", "puzzle", "computer", "science", "syntax",
    "compile", "debug", "execute", "algorithm", "binary",
    "network", "storage", "memory", "object", "class",
    "inherit", "method", "recursion", "array", "module",
    "branch", "commit", "merge", "server", "client",
    "cookie", "thread", "socket", "router", "packet",
    "encrypt", "decrypt", "boolean", "console", "editor",
    "github", "script", "pointer", "kernel", "driver",
    "upload", "download", "float", "double", "random",
    "global", "static", "define", "inline", "lambda",
    "import", "export", "return", "switch", "case",
    "break", "continue", "exception", "try", "catch",
    "finally", "assert", "virtual", "abstract", "keyword",
    "package", "library", "terminal", "source", "buffer",
    "debugger", "logic", "process", "threading", "command",
    "cursor", "interface", "database", "backend", "frontend",
    "firewall", "bandwidth", "protocol",
    "apple", "banana", "grapes", "orange", "peach",
    "mango", "kiwi", "lemon", "cherry", "melon",
    "zebra", "tiger", "lion", "giraffe", "elephant",
    "rabbit", "monkey", "donkey", "panda", "koala",
    "doctor", "teacher", "farmer", "painter", "chef",
    "nurse", "singer", "dancer", "pilot", "actor",
    "ocean", "desert", "island", "valley", "mountain",
    "forest", "jungle", "river", "canyon", "volcano",
    "school", "temple", "village", "palace", "market",
    "bottle", "mirror", "pillow", "blanket", "candle",
    "window", "ladder", "bucket", "hammer", "screwdriver",
    "pencil", "eraser", "notebook", "marker", "scissors",
    "breakfast", "dinner", "lunch", "burger", "pizza",
    "sandwich", "salad", "cookie", "biscuit", "noodle",
    "country", "city", "street", "bridge", "station",
    "garden", "museum", "zoo", "airport", "hotel",
    "circle", "triangle", "square", "rectangle", "hexagon",
    "whistle", "guitar", "violin", "trumpet", "drum",
    "rainbow", "sunshine", "cloud", "storm", "breeze",
    "summer", "winter", "autumn", "spring", "snowfall"
]

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

lives = 6

game_over = False

correct_letters = []

while not game_over :

    guess = input(f"Guess a letter:").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}, Try something else.  ")

    display = ""

    for letter in chosen_word:

        if letter == guess:
            correct_letters += letter
            display += letter

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(f"You Guessed: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.You loose a life.")
        if lives == 0:
            game_over = True
            print(f"No lives left,You Loose, The word was {chosen_word}")

    if "_" not in display:
        print("You win")
        game_over = True

    print(stages[lives])