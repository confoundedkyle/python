# Arrays - used for simple data types, must all be the same type
# https://github.com/microsoft/c9-python-getting-started/tree/master/11%20-%20Collections

from array import array
scores = array('d')
scores.append(97)
scores.append(90)
print(scores)
print(scores[1])

# Common Operators

names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)


# Retrieving Ranges

names = ['Susan', 'Christopher', 'Bill']
presenters = names[0:2] # Get the first two items
# Starting index and number of items to retrieve

print(names)
print(presenters)
