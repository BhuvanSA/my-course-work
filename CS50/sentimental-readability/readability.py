# TODO

s = input("Text: ")
letters = 0
words = 1
sentences = 0
leng = len(s)
pun = ['.', '!', '?']
for letter in s:
    if letter.isalpha():
        letters += 1
    if letter.isspace():
        words += 1
    if letter in pun:
        sentences += 1

L = (letters / words) * 100  # Calculating L
S = (sentences / words) * 100  # Calculating S
index = 0.0588 * L - 0.296 * S - 15.8  # Calculating index
rounded = round(index)
if rounded < 1:
    print("Before Grade 1")

elif rounded >= 16:
    print("Grade 16+")

else:
    print("Grade ", rounded)  # Printing the rounded Value
