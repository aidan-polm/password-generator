import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters do you want to include?"))
nr_numbers = int(input("How many numbers do you want to include?"))
nr_symbols = int(input("How many symbols do you want to include?"))

password_char = []
password = ""

for char in range(1, nr_letters + 1):
    new_letter = random.choice(letters)
    password_char.append(new_letter)
    
for num in range(1, nr_numbers + 1):
    new_num = random.choice(numbers)
    password_char.append(new_num)
    
for sym in range(1, nr_symbols + 1):
    new_sym = random.choice(symbols)
    password_char.append(new_sym)

for item in range(1, len(password_char) + 1):
    new_pass = random.choice(password_char)
    password_char.remove(new_pass)
    password += new_pass
    
print(password)