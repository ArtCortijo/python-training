# lesson 09 - reusable blocks of code
# naming convention: all lowercase with underscores
def hello_world():
    print('Hello world!')


hello_world()


def sum(num1=1, num2=4):
    if (type(num1) != int or type(num2) != int):
        print('You must provide two numbers')
        return
    return num1 + num2


# print(sum('a', 3))

# print(sum(3, 3))
total = sum(3, 3)
print(total)


# use * when you don't know how many arguments will be passed to a function
def multiple_items(*args):
    print(args)  # tuple (Tuples are used to store multiple items in a single variable)
    print(type(args))
    # for item in args:
    #     print(item)


multiple_items('apple', 'banana', 'cherry')


# kwargs = key word arguments
def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first='Art', last='Cortijo')
