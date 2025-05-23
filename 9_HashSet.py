# HashSet (no duplicates)
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet)) # length

print(1 in mySet) # search

mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1, 2, 3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)