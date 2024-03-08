import random
import sys


def get_input(s):
    while True:
        try:
            level = int(input(s).strip())
        except EOFError:
            sys.exit()
        except:
            continue

        if level > 0:
            return level


level = get_input("Level: ")

randi = random.randint(1, level)

while True:
    guess = get_input("Guess: ")
    if guess == randi:
        sys.exit("Just right!")
    elif guess > randi:
        print("Too large!")
    else:
        print("Too small!")
