from datetime import date
import inflect
import sys


def main():
    print(age_in_mins(input("Date of Birth: ")))


def age_in_mins(data: str):
    try:
        data = data.strip()
        birth_date = date.fromisoformat(data)
    except:
        sys.exit('Invalid Date')
    else:
        p = inflect.engine()
        date_today = date.today()
        timeDelta = date_today - birth_date
        min_int = str(timeDelta.days * 24 * 60)
        why = p.number_to_words(min_int, andword='')
        why = why.capitalize() + " minutes"
        return why


if __name__ == "__main__":
    main()
