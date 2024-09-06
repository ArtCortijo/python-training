# lesson 08
value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('Loop is done ' + str(value))

# names = ['John', 'Paul', 'George', 'Ringo']

# for name in names:
#     print(name)

# for letter in 'Hello':
#     print(letter)

# for name in names:
#     if name == 'George':
#         break
#     print(name)

# print("")

# for name in names:
#     if name == 'George':
#         continue
#     print(name)

# for x in range(4):
#     print(x)

# print("")

# for x in range(2, 4):
#     print(x)

for x in range(0, 100, 5):
    print(x)
else:
    print('Loop is done ' + str(x))

print("")

names = ['Art', 'Bob', 'Charlie']
actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(name + ' ' + action)
    print('---')

for action in actions:
    for name in names:
        print(name + ' ' + action)
    print('---')
