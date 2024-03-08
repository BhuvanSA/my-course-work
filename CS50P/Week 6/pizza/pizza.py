import sys
from tabulate import tabulate
import csv


def main():
    file_path = get_file_path()
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            header = row
            break
        print(tabulate(reader, header, tablefmt="grid"))


def get_file_path():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        assert sys.argv[1].split(".")[1] == "csv"
    except:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as f:
            ...
    except:
        sys.exit("File does not exist")

    return sys.argv[1]


if __name__ == "__main__":
    main()
