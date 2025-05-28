# Arrays & Hashing

### Day 1

## Contains Duplicate

I did it in python3. As soon as I heard unique identifier in the list, I thought of **HashSet**. Since, HashSet keeps track of unique items, I just needed to compare the added unique items to the original nums array. Simply, I just checked when I added an item to a HashSet if the item existed in the set. The in operation in a set takes O(1) operation time, since we iterated through all the items in lists, the time complexity is O(n). Since we used a HashSet to store all of it, the space complexity is O(n)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in range(len(nums)):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                return True
        return False
```

Time Complexity: O(n)

Space Complexity: O(n)

## Valid Anagram

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map each alphabet with a cnt integer for s
        sMap = defaultdict(int)
        for i in range(len(s)):
            sMap[s[i]] += 1

        # do the same for t
        tMap = defaultdict(int)
        for i in range(len(t)):
            tMap[t[i]] += 1

        # check if the two HashMap is the same
        return sMap == tMap
```

Time Complexity: O(n)

Space Complexity: 3O(n) = O(n)

## Two Sum

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap to store number -> index
        numMap = {}
        
        # One pass through the array
        for i, num in enumerate(nums):
            # find the complement and check if that exists in the HashMap
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            # add it to the dict if the complement of the thing doesn't exist
            numMap[num] = i
            
        return []  # No solution found
```

Time Complexity: O(n)

Space complexity: O(n)

### Day 2

## Group Anagrams

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted(word) as key and the value as lists of indexes of the 
        # original array that had the same sorted array
        myMap = defaultdict(list)
        for i, word in enumerate(strs):
            # but then a list is not hashable so use a tuple
            myMap[tuple(sorted(word))].append(i)

        # make the outer array and made the inner arrays blank
        arr = [[] for _ in range(len(myMap))]

        # I just appended all the original values into the list of lists
        cnt = 0
        for key in myMap:
            retrieve = myMap[key]
            for index in retrieve:
                arr[cnt].append(strs[index])
            cnt += 1
        
        return arr
```

optimized version:
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            finalWord = ''
            for key in sorted(word):
                finalWord+=key
            map[finalWord].append(word)
        return list(map.values()) # key function I didn't know about, you can return list of values
```

Time Complexity: O(n * k * log k)
- n is number of strings
- k is length of longest string
- Dominated by sorting each string (k log k) done n times

Space Complexity: O(n * k)
- n is number of strings
- k is length of longest string
- Need to store all strings in both map and result array

## Top K Frequent Elements

** BUCKET SORT **