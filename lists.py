# lesson06 - Lists & Tuples
users = ['Art', 'Bob', 'Mia']
data = ['Art', '42', True]
empytList = []

print('Art' in users)

print(users[0])
print(users[-1])

print(users.index('Mia'))

print(users[0:2])
print(users[1:])

# returns length of list
print(len(users))

users.append('Elvis')
print(users)

# Make sure you're using a list
users += ['Dolly']
print(users)

# users.extend(['Rob', 'Sue'])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Sara')
print(users)

# Insert at the 2nd index
users[2:2] = ['Bleh', 'Blah']
print(users)

# Replace values
users[1:3] = ['Lili', 'Lulu']
print(users)

users.remove('Sara')
print(users)

# Remove last item
print(users.pop())
print(users)

# Remove first item
del users[0]
print(users)

data.clear()
print(data)

# when it's lowercase, it comes after uppercase
users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 8, 16, 23, 15]
nums.reverse()
print(nums)

# Descending order
# nums.sort(reverse=True)
# print(nums)

# This does not modify the original list
print(sorted(nums, reverse=True))

# All three of these are copies of the original list
numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]
print('Copies')
print(nums)
print(numsCopy)
print(myNums)
print(myCopy)

# Tuples are like lists, but they are immutable (do not change)
myTuple = tuple(('Art', '40', True))
anotherTuple = (1, 4, 2, 3, 5)
print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append('Luke')
newTuple = tuple(newList)
print(newTuple)

(one, two, *hey) = anotherTuple
print(one)
print(two)
print(hey)
