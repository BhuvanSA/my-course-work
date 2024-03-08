import random
import sys


def main():
    level = get_level()
    score = 10
    for i in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        s = x + y
        for j in range(4):
            if j == 3:
                print(f"{x} + {y} = {s}")
                score -= 1
                break
            print(f"{x} + {y} = ", end="")
            try:
                u = int(input().strip())
            except EOFError:
                sys.exit()
            except:
                print("EEE")
                continue
            if u == s:
                break
            else:
                print("EEE")
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
        except EOFError:
            sys.exit()
        except:
            continue
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("level can only be 1-3 given")


if __name__ == "__main__":
    main()
