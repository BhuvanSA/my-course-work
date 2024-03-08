def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum() and number_check(s):
        return True
    return False


def number_check(s):
    # If all digits are alpabets no need to check numbers
    # so return True
    if s.isalpha():
        return True

    for i, ch in enumerate(s):
        if ch.isdigit():
            number = s[i:]
            if number.isdigit() and int(number[0]) != 0:
                return True
            else:
                break

    return False


if __name__ == "__main__":
    main()
