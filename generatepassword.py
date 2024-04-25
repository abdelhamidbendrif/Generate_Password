#By Abdelahmid 2024
import string
import random

store1 = list(string.ascii_lowercase)
store2 = list(string.ascii_uppercase)
store3 = list(string.digits)
store4 = list(string.punctuation)

user_input = input("Number of characters for your password: ")

while True:
    try:
        nbr_characters = int(user_input)

        if nbr_characters < 8:
            print("Your password must be at least 8 characters long.")
            user_input = input("Please enter the number of characters for your password again: ")
        else:
            break
    except ValueError:
        print("Please enter numbers only.")
        user_input = input("Specify the number of characters for your password: ")

# Shuffle all the lists
random.shuffle(store1)
random.shuffle(store2)
random.shuffle(store3)
random.shuffle(store4)

part1 = round(nbr_characters * (40/100))
part2 = round(nbr_characters * (30/100))
part3 = round(nbr_characters * (20/100))
part4 = nbr_characters - part1 - part2 - part3

results = []

# Append characters from each category
for y in range(part1):
    results.append(store1[y])
for y in range(part2):
    results.append(store2[y])
for y in range(part3):
    results.append(store3[y])
for y in range(part4):
    results.append(store4[y])

# Shuffle the final password
random.shuffle(results)

password = "".join(results)
print("Your password is:", password)
