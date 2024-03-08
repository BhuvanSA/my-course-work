# Inputting data
data = input("Input: ").strip()

# Declaring vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Checking if letter is a vowel
for letter in data:
    if letter.lower() in vowels:
        continue
    else:
        print(letter, end="")

# Add /n after printing all chars
print()
