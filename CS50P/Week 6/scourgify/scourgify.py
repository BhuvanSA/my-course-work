import sys
import csv


def main():
    data = []
    before, after = get_file_path()
    with open(after, "w") as write:
        writer = csv.writer(write)
        writer.writerow(["first", "last", "house"])
    with open(before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(",")
            house = row['house']

            with open(after, "a") as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([first.strip(), last.strip(), house.strip()])


def get_file_path():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        assert sys.argv[1].split(".")[1] == "csv"
        assert sys.argv[2].split(".")[1] == "csv"
    except:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as f:
            ...
    except:
        sys.exit("Could not read " + sys.argv[1])

    return [sys.argv[1], sys.argv[2]]


if __name__ == "__main__":
    main()
