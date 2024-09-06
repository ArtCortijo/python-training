# lesson 10 - recursion: when a function calls itself
def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


myNewTotal = add_one(0)
print(myNewTotal)


# example
value = True
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = False  # or = 0 also means False
        continue
