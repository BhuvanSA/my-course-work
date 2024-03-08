# A function which replaces
def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


# Takes input calls convert function and prints it
print(convert(input()))
