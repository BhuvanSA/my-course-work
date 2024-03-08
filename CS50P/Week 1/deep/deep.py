# Taking input from user and lowering it and stripping white spaces
data = input(
    "What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# match case for the data
match data:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
