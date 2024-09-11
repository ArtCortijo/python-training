# Lesson 22 - Files Operations
import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if file does not exist
# file = open('names.txt', 'r')
file = open('names.txt')
# print(file.read())
# print(file.read(3))  # reads the first 3 characters

# print(file.readline())  # reads the first line
# print(file.readline())  # reads the second line

for line in file:
    print(line)

file.close()  # always close the file after opening it

try:
    file = open('names.txt')
    print(file.read())
except FileNotFoundError as error:
    print(f'\nFile not found: {error}')
finally:
    file.close()
# better way to do this ☝️, look at line 67

# Append - creates a file if it does not exist
file = open('names.txt', 'a')
file.write('\nTommy')
file.close()

file = open('names.txt')
print(file.read())
file.close()

# Write (overwrite) - creates a file if it does not exist
file = open('context.txt', 'w')
file.write('I deleted all of the context.')
file.close()

file = open('context.txt')
print(file.read())
file.close()

# Two ways to create a new file

# Opens a file for writing and creates it if it does not exist
file = open('new_file.txt', 'w')
file.close()

# Creates the specified file and returns an error if it already exists
if not os.path.exists('art.txt'):  # checks if the file art.txt does not exist
    file = open('art.txt', 'x')
    file.close()

# Delete a file
# avoid an error if the file does not exist
if os.path.exists('art.txt'):
    os.remove('art.txt')
else:
    print('The file you wish to delete does not exist.')


with open('more_names.txt') as file:
    content = file.read()

# Basically copying the content of more_names.txt to names.txt
with open('names.txt', 'w') as file:
    file.write(content)
