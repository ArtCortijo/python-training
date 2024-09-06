# Lesson 13 - f-strings (formatted string literals) to simplify string formatting and interpolation.
# https://www.w3schools.com/python/ref_string_format.asp

person = "Art"
coins = 3

# print("\n" + person + " has " + str(coins) + " coins left")
# message = "\n%s has %s coins left" % (person, coins)
# message = "\n{} has {} coins left".format(person, coins)
# message = "\n{1} has {0} coins left".format(person, coins)  # reverse order
# message = "\n{person} has {coins} coins left".format(coins=coins, person=person)

# dictionary
player = {'person': 'Art', 'coins': 3}
# message = "\n{person} has {coins} coins left".format(**player)
# print(message)

# f-string
message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person} has {2*5} coins left"
print(message)

message = f"\n{person.lower()} has {2*5} coins left"
print(message)

message = f"\n{player['person']} has {player['coins']} coins left"
print(message)

# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25*num:.2f}")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25*num:.2f}")

for num in range(1, 11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")
