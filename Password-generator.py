import random

# Lists of possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduction message
print("Welcome to the PyPassword Generator!")

# User input for number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store password components
password_list = []

# Add random letters to the password list
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# Add random numbers to the password list
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# Print the unshuffled password list
print(password_list)

# Shuffle the list to ensure the password components are mixed
random.shuffle(password_list)

# Print the shuffled list to show the random order
print(password_list)

# Combine the shuffled components into a single string
password = ""
for char in password_list:
  password += char

# Output the final password
print(f"Your password is: {password}")

# Tests
assert len(password) == nr_letters + nr_symbols + nr_numbers, "Error: Password length is incorrect."
assert sum(c in letters for c in password) == nr_letters, "Error: Number of letters in the password is incorrect."
assert sum(c in symbols for c in password) == nr_symbols, "Error: Number of symbols in the password is incorrect."
assert sum(c in numbers for c in password) == nr_numbers, "Error: Number of numbers in the password is incorrect."

print("All tests passed!")

