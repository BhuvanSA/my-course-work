months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip().split("/")
        if len(date) == 3:
            month, day, year = int(date[0]), int(date[1]), int(date[2])
            if month > 12 or day > 31:
                continue
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        date = date[0].split(" ")
        if len(date) == 3:
            month, day, year = date[0].title(), int(date[1][:-1]), int(date[2])
            if month not in months or day > 31:
                continue
            print(f"{year:04d}-{months.index(month)+1:02d}-{day:02d}")
            break
    except EOFError:
        break
    except:
        ...
