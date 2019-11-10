# 25 of 44 - Collections
# https://www.youtube.com/watch?v=GWVrLL2BulM&list=PL_KpcT9HZRVXsGXOtgS5FsnDFxJV8mRmw&index=25

# Lists
# Lists are a collection in items

names = ['Christopher', 'Susan']
print(names)

# Empty Lists can be used with []

scores = []
scores.append(98) # Add net item to the end
scores.append(99)
print(scores)
print(scores[1]) # Collections are zero-indexed (counting starts at 0)

# Arrays

from array import array
scores = array('d')
scores.append(97)
scores.append(90)
print(scores)
print(scores[1])
 