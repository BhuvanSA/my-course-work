# TODO
# A function to find the checksum value of a list
def checksum(list):
    copy = []
    for x in range(len(list)):  # copying and creating a new list
        copy.append(list[x])
    flag = False
    sum = 0
    for x in range(2, len(copy)+1, 2):  # multiplytin by 2
        copy[-x] = copy[-x] * 2

    for x in range(0, len(list), 1):
        copy[x] = summer(copy[x])

    for x in range(len(copy)):  # finding sum
        sum += copy[x]

    if sum % 10 == 0:  # checksum
        flag = True
    return flag

# A function to sum two digit number in array


def summer(number):
    num = str(number)
    sum = 0
    for x in range(len(num)):
        sum = sum + int(num[x])
    return sum


def inp():  # A fucntion to take proper input from the user
    list = []
    inp = None
    while True:
        inp = input("Number: ")
        if inp.isnumeric():
            break
    for x in inp:
        list.append(int(x))
    return list


list = inp()
flag = checksum(list)
leng = len(list)

if flag and leng == 15 and list[0] == 3 and (list[1] == 4 or list[1] == 7):  # checking for amex
    print("AMEX")

elif flag and leng == 16 and list[0] == 5 and (list[1] > 0 and list[1] < 6):  # chekcing for mastercard
    print("MASTERCARD")

elif flag and (leng == 13 or leng == 16) and list[0] == 4:  # cheking for visa
    print("VISA")
else:  # else case invalid
    print("INVALID")

