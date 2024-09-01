import math
# lesson04

# String data type

# Literal assignment
first = "Arturo"
last = "Cortijo"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
full_name = first + ' ' + last
print(full_name)

full_name += '!'
print(full_name)

# Casting a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I like punk rock from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey, how are you? 

I was just checking in.
             All good?
"""
print(multiline)

# Escaping special characters
sentence = 'I\'m a dev\tHey!\n\nWhere\'s the rest of the\\staff?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('Hey', 'Hello'))

print(len(multiline))
multiline += "                                 "
multiline = "                 " + multiline
print(len(multiline))

# removing the white space
print(len(multiline.strip()))
# removing the white space from the left side
print(len(multiline.lstrip()))
# removing the white space from the right side
print(len(multiline.rstrip()))

print('')

# Build a menu
title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, '.') + '$1'.rjust(4))
print("Muffin".ljust(16, '.') + '$2'.rjust(4))
print("Cheesecake".ljust(16, '.') + '$4'.rjust(4))

# String index values
print(first[1])
# get the last character
print(first[-1])
print(first[0:-1])
print(first[0:])

# Some methods return boolean data
print(first.startswith('A'))
print(first.endswith('Z'))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

# Integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float
gpa = 3.5
y = float(1.14)
print(type(gpa))

# Complex
comp_value = 3 + 4j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print('')

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print('')

print(math.pi)
print(math.sqrt(16))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = '10001'
zip_num = int(zipcode)
print(type(zip_num))

# Error if you attempt to cast incorrect data
zip_num = int('Hello')
