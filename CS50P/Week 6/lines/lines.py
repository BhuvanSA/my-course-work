import sys


def main():
    file_path = get_file_path()

    line_count = 0
    with open(file_path) as file:
        for line in file:
            if len(line.strip()) > 0:
                if line.strip()[0] != "#":
                    line_count += 1
        print(line_count)


def get_file_path():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        assert sys.argv[1].split(".")[1] == "py"
    except:
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as f:
            ...
    except:
        sys.exit("File does not exist")

    return sys.argv[1]


if __name__ == "__main__":
    main()
