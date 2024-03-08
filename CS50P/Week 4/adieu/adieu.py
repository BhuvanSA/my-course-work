
names = []

while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except:
        break

print("Adieu, adieu, to", end=" ")

lastName = names[-1]
for name in names:
    if len(names) > 2 and lastName == name:
        print("and", lastName)
        break
    elif len(names) == 1:
        print(name)
        break
    elif len(names) == 2:
        print(name + " and " + lastName)
        break
    print(name, end=", ")
print()
