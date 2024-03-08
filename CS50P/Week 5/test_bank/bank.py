def main():
    data = input("Greeting: ").strip()
    print(f"${value(data)}")


def value(data):
    data = data.lower()
    # Checking if the first five letters is hello
    if data[:5] == "hello":
        return 0
    elif data[0] == 'h':  # Checking if first letter is h
        return 20
    else:  # 100 dollar
        return 100


if __name__ == "__main__":
    main()
