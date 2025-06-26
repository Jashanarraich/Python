print("Welcome to the password generator.\n")

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '"', '#', '$', '%', '&',
]

nr_alphabets = int(input("Enter the number of alphabets you want:\n"))
nr_numbers = int(input("Enter the number of numbers you want:\n"))
nr_symbols = int(input("Enter the number of symbols you want:\n"))

password_list = []

for choice in range(0, nr_alphabets):
    password_list += random.choice(alphabets)

for choice in range(0, nr_numbers):
    password_list += random.choice(digits)

for choice in range(0, nr_symbols):
    password_list+=random.choice(symbols)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is {password}")
