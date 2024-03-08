def main():
    # Processing user input
    data = input("What time is it? ").strip()
    time = convert(data)
    # print(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")


# converts entered time to a floting point digit
def convert(time):
    time = time.split(":")
    return (float(time[0]) + float(time[-1]) / 60)


if __name__ == "__main__":
    main()
