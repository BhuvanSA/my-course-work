import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str):
    count = 0
    ip = ip.strip()
    if m := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        lis = [0 <= int(x) <= 255 for x in m.group(1, 2, 3, 4)]
        for val in lis:
            if val:
                count += 1

    if count > 3:
        return True

    else:
        return False


...


if __name__ == "__main__":
    main()
