# Reverse
nums = [1, 2, 3]
nums.reverse()  # O(n)
print(nums)

# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()  # O(n log n)
print(arr)

arr.sort(reverse=True)  # O(n log n)
print(arr)

# Sort in alphabetical order
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x:len(x)) # lambda functions are just unnamed functions

# List comprehension
arr = [i for i in range(5)]
print(arr)

# 2-D lists (arrays)
arr = [[0] * 4 for i in range(4)]

# This won't work as each row has the same reference
arr = [[0] * 4] * 4
print(arr)
