import emoji

data = input("Input: ").strip()
print(emoji.emojize(data, language="alias"))
