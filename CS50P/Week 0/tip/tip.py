def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d[1:]
    print(float(d))
    return float(d)


def percent_to_float(p):
    # TODO
    p = float(p[:-1])
    print(p/100)
    return p/100


main()
