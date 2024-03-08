import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str):
    if m := re.search(r"^<iframe.*src=\"(.+(www.)?youtube.com/embed[^ ]+)\".*>$", s):
        m = m.group(1)
        m = re.sub(r"https?://(www\.)?youtube\.com/embed",
                   "https://youtu.be", str(m))
        return m

    ...


...


if __name__ == "__main__":
    main()
