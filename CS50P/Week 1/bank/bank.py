# Cleaning the input data
data = input("Greeting: ").lower().strip()

# Checking if the first five letters is hello
if data[:5] == "hello":
    print("$0")
elif data[0] == 'h':  # Checking if first letter is h
    print("$20")
else:  # 100 dollar
    print("$100")
