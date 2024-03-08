# Taking a processing input data
data = input("camelCase: ").strip()

# Accessing every letter from the given string
for letter in data:
    if letter.islower():
        print(letter, end="")
    else:
        print("_" + letter.lower(), end="")

# Printing /n after the word is printed
print()
