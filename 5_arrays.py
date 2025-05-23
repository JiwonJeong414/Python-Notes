# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack 
arr.append(4)
arr.append(5)
print(arr)

arr.pop() # Big O(1) operation
print(arr)

arr.insert(1, 7) # Big O(n) operation
print(arr)

arr[0] = 0 # Big O(1) operation indexing
arr[3] = 0
print(arr)

# Intialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds, 
# it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc. 

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# Similar to for-loop ranges, last index is 
# non-inclusive
print(arr[0:4])

# Unpacking
a, b, c = [1,2,3]
print(a, b, c)

# Be careful though
# a, b = [1,2,3] this doesn't work, it has to match

# Loop through arrays
nums = [1,2,3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays stimultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)