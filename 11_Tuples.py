# Tuples are like array but immutable (like final arrays in java)
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify

# Can be used as key for hash map/set
myMap = {(1, 2) : 3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1, 2) in mySet)

# The reason for doing is that
# Lists can't be keys
# myMap[[3,4]] = 5 doesn't work