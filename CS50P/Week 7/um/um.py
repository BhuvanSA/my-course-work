import re
# import sys


def main():
    print(count(input("Text: ")))


def count(s: str):
    s = s.strip()
    s = f" {s} "
    um_list = re.findall(r" um[ ,.?]", s, re.IGNORECASE)
    return len(um_list)
    ...


...


if __name__ == "__main__":
    main()
