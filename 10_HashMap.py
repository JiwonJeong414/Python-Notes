# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap)) # length of HashMap

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice" : 90, "bob" : 70}
print(myMap)

# Dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

# Looping through maps
myMap = {"alice" : 90, "bob" : 70}
for key in myMap:
    print(key, myMap[key])

# just values
for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# While Loops in Python
# Basic while loop
i = 0
while i < 5:
    print(i)
    i += 1

# While loop with break
i = 0
while True:
    if i == 5:
        break
    print(i)
    i += 1

# While loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# While loop with else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished!")

# While loop for finding something
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] == 3:
        print("Found 3!")
        break
    i += 1

# defaultdict - automatically handles missing keys
from collections import defaultdict

# Regular dictionary - need to check if key exists
regular_dict = {}
# regular_dict["count"] += 1  # This would raise KeyError

# defaultdict with int - automatically initializes to 0
count_dict = defaultdict(int)
count_dict["count"] += 1  # Works! Automatically starts at 0
print(count_dict["count"])  # 1

# defaultdict with list - automatically initializes to empty list
list_dict = defaultdict(list)
list_dict["numbers"].append(1)  # Works! Automatically creates empty list
print(list_dict["numbers"])  # [1]

# defaultdict with set - automatically initializes to empty set
set_dict = defaultdict(set)
set_dict["unique"].add(1)  # Works! Automatically creates empty set
print(set_dict["unique"])  # {1}

# Common use case: counting occurrences
word = "hello"
char_count = defaultdict(int)
for char in word:
    char_count[char] += 1  # No need to check if key exists
print(char_count)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Without defaultdict, you'd need to write:
char_count = {}
for char in word:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

# Hashmap functions
print(myMap.get("alice", 0))  # 88
print(myMap.get("charlie", 0))  # 0 (default value if key doesn't exist)

# Check if key exists
if "alice" in myMap:
    print("alice exists")

# Remove key-value pair
myMap.pop("alice")
print(myMap)

# Clear hashmap
myMap.clear()
print(myMap)

# duplicate

if number in myMap[i]:
    print(false)