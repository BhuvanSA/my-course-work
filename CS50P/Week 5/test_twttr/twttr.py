# Declaring vowels
vowels = ['a', 'e', 'i', 'o', 'u']


def main():
    data = input("Input: ").strip()
    print(shorten(data))
    ...


def shorten(word):
    # Checking if letter is a vowel
    s = ""
    for letter in word:
        if letter.lower() in vowels:
            continue
        else:
            s += letter
    return s


if __name__ == "__main__":
    main()
