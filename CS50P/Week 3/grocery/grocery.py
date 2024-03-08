a = dict()

while True:
    try:
        data = input().strip().upper()
    except EOFError:
        print()
        break

    if data not in a:
        a[data] = 1
    else:
        a[data] += 1

for key, value in sorted(a.items()):
    print(f"{value} {key}")
