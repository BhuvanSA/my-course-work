# setting initial due
amount_due = 50

# making it execute until due is <= 0
while amount_due > 0:
    print("Amount Due:", amount_due)
    data = int(input("Insert Coin: ").strip())

    if data in [25, 10, 5]:
        amount_due -= data

# print change owed if coin inserted is greater than inital due
print("Change Owed:", abs(amount_due))
