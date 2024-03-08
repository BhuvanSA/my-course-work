def main():
    x, y = get_inp()
    per = (float(x) / float(y)) * 100
    if per <= 1:
        print("E")
    elif per >= 99:
        print("F")
    else:
        print(str(round(per))+"%")


def get_inp():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            assert x <= y
            assert y != 0

        except KeyboardInterrupt:
            # print("something went wrong")
            break
        except:
            ...
        else:
            return int(x), int(y)


if __name__ == "__main__":
    main()
