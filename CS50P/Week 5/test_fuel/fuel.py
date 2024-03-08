def main():
    print(gauge(convert(input())))


def convert(fraction):
    x, y = fraction.split("/")
    per = (int(x) / int(y)) * 100
    if int(x) > int(y):
        raise ValueError

    return round(per)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage))+"%"


if __name__ == "__main__":
    main()
