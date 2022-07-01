import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
password = ''

for iteration in range(1, nr_letters + 1):
    letter = random.choice(letters)
    password += letter
for iteration in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password += symbol
for iteration in range(1, nr_numbers + 1):
    number = random.choice(numbers)
    password += number

print(password)


#Hard Level
password_list = []
for iteration in range(1, nr_letters + 1):
    letter = random.choice(letters)
    password_list += letter
for iteration in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password_list += symbol
for iteration in range(1, nr_numbers + 1):
    number = random.choice(numbers)
    password_list += number

random.shuffle(password_list)

hard_password = ''
for char in password_list:
    hard_password += char

print(hard_password)
