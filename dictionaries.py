# lesson 07
# Dictionaries are used to store data values in key:value pairs (object in JS).
band = {
    'vocals': 'Plant',
    'guitar': 'Page',
}

# Use the constructor function dict
band2 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)
print(type(band))
print(len(band))

# Accessing Items
print(band['vocals'])
print(band.get('guitar'))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List all key:value pairs as tuples
print(band.items())

# Verifying if a key exists in a dictionary
print('vocals' in band)
print('bass' in band)

# Change values
band['vocals'] = 'Cobain'
band.update({'bass': 'Fat Mike'})
print(band)

# Remove items
print(band.pop('bass'))
print(band)

band['drums'] = 'Grohl'
print(band)

# Remove the last item that was added and returns it as a tuple
# print(band.popitem())  # Tuple
# print(band)

# Delete and clear
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band  # This is not a copy, it's a reference
# print('Bad copy')
# print(band2)
# print(band)

# band2['drums'] = 'Metal'
# print(band)

band2 = band.copy()  # This is a copy and not a reference
band2['drums'] = 'Metal'
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print(band3)


# Nested dictionaries
member1 = {
    'name': 'Plant',
    'instrument': 'vocals',
}

member2 = {
    'name': 'Page',
    'instrument': 'guitar',
}

band = {
    'member1': member1,
    'member2': member2,
}

print(band)
print(band['member1']['name'])

# Sets
# Sets are used to store multiple items in a single variable.

nums = {1, 2, 3, 4, 5}
nums2 = set([1, 2, 3, 4, 5])

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 3, 4, 5, 5, 5}
print(nums)

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
moreNums = {5, 6, 7}
nums.update(moreNums)
print(nums)

# You can use update with lists, tuples and dictionaries too

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

myNewSet = one.union(two)
print(myNewSet)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except dupicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
