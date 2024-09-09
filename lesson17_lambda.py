# Lesson 17 - Lambda & Higher Order Functions
# reduce() function is defined in the functools module. It applies a function of two arguments cumulatively to the items of an iterable, optionally starting with an initial argument. It has the following syntax:
from functools import reduce


def squared(num): return num * num  # lambda num: num * num


print(squared(2))


def addTwo(num): return num + 2  # lambda num: num + 2


print(addTwo(12))


def sumTotal(a, b): return a + b  # lambda a, b: a + b


print(sumTotal(3, 4))


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

############################################################

# Higher Order Functions: Functions that take other functions as arguments or return functions as their result.
numbers = [3, 7, 12, 18, 20, 21]

# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# filter() function constructs an iterator from elements of an iterable for which a function returns true.
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

numbers = [1, 2, 3, 4, 5, 1]

# reduce() function is defined in the functools module. It applies a function of two arguments cumulatively to the items of an iterable, optionally starting with an initial argument (10 in the example below).
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers))


names = ['Art', 'Bob', 'Charlie', 'David', 'Ed']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
