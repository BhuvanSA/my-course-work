
import re
# import sys


def main():
    print(convert(input("Hours: ")))


def convert(s: str):
    if m := re.search(r"(\d(?:\d)?)(?::(\d\d))? (AM|PM) to (\d(?:\d)?)(?::(\d\d))? (AM|PM)", s, re.IGNORECASE):
        # if m := re.search(r"(\d(\d)?)", s):
        # print(m.groups())
        start_hour: int = int(m.group(1))
        start_min: int = int(m.group(2) if m.group(2) else "00")
        start_m: str = m.group(3)
        end_hour: int = int(m.group(4))
        end_min: int = int(m.group(5) if m.group(5) else "00")
        end_m: str = m.group(6)

        check(start_hour, start_min, end_hour, end_min)

        start_hour = hour_convert(start_m, start_hour)
        end_hour = hour_convert(end_m, end_hour)

        return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"
    raise ValueError("Invalid format")


def hour_convert(m: str, hour: int) -> int:
    if hour == 12:
        if m == "AM":
            return 00
        else:
            return 12
    if m == 'PM':
        return hour + 12
    return hour


def check(start_hour: int, start_min: int, end_hour: int, end_min: int):
    if not 0 < int(start_hour) <= 12 or not 0 < int(end_hour) <= 12:
        raise ValueError("Hour value not in range of 1-12")
    if not 0 <= int(start_min) < 60 or not 0 <= int(end_min) < 60:
        raise ValueError("Mins value not in range of 00-59")


if __name__ == "__main__":
    main()
