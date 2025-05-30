from typing import List
from collections import defaultdict

def encode(strs: List[str]) -> str:
        output = ""
        for words in strs:
            output += str(len(words)) + "#" + words  # Add delimiter
        return output

def decode(s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            j = s.find('#', i)  # Find '#' starting from position i
            length = int(s[i:j])
            original.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return original

def encode2(strs: List[str]) -> str:
        output = ""
        for words in strs:
            output += str(len(words)) 
            output += words
        return output

def decode2(s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            # Get the length of the next word
            length = int(s[i])
            # Get the word starting after the length
            word = s[i+1:i+1+length]
            original.append(word)
            # Move to next word
            i += 1 + length
        return original

def safe_division(nums: List[int]) -> List[float]:
    output = []
    product = 1
    for i in range(len(nums) - 1):  # Stop one index before the end
        output.append(product * (nums[i]/nums[i + 1]))
    return output

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and combine with prefix
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    
    return output

def has_duplicate_using_in(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:  # Check if number is already in set
            return True
        seen.add(num)    # Add number to set
    return False

def has_duplicate_using_len(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))  # If lengths are different, there's a duplicate

def isValidSudoku(board: List[List[str]]) -> bool:
    myMap = defaultdict(set)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":  # Skip empty cells
                continue
                
            # Create tuple keys for row, column, and box
            row_key = (i, -1)
            col_key = (-1, j)
            box_key = (i // 3, j // 3)
            
            # Check if number exists in row, column, or box
            if board[i][j] in myMap[row_key]:
                return False
            if board[i][j] in myMap[col_key]:
                return False
            if board[i][j] in myMap[box_key]:
                return False
                
            # Add number to corresponding sets
            myMap[row_key].add(board[i][j])
            myMap[col_key].add(board[i][j])
            myMap[box_key].add(board[i][j])
    
    return True

def find_max_value_examples():
    # Example dictionary
    my_map = {'a': 5, 'b': 10, 'c': 3, 'd': 8}
    
    # Method 1: Using max() with values()
    max_value1 = max(my_map.values())
    print(f"Method 1 - max value: {max_value1}")  # 10
    
    # Method 2: Using max() with items() to get both key and value
    max_key, max_value2 = max(my_map.items(), key=lambda x: x[1])
    print(f"Method 2 - max key: {max_key}, max value: {max_value2}")  # b, 10
    
    # Method 3: Using a loop (more explicit)
    max_value3 = float('-inf')
    for value in my_map.values():
        max_value3 = max(max_value3, value)
    print(f"Method 3 - max value: {max_value3}")  # 10
    
    # Method 4: If you need the key with the highest value
    max_key2 = max(my_map, key=my_map.get)
    print(f"Method 4 - key with max value: {max_key2}")  # b

def defaultdict_example():
    # Incorrect way:
    # myMap = defaultdict(0)  # This will raise TypeError
    
    # Correct way:
    myMap = defaultdict(int)  # This creates a defaultdict that defaults to 0
    
    # Example usage
    myMap['a'] += 1  # No need to check if key exists
    myMap['b'] += 1
    print(f"myMap['a']: {myMap['a']}")  # 1
    print(f"myMap['b']: {myMap['b']}")  # 1
    print(f"myMap['c']: {myMap['c']}")  # 0 (default value)
    
    # Alternative ways to create a defaultdict with default 0:
    # Method 1: Using lambda
    myMap2 = defaultdict(lambda: 0)
    
    # Method 2: Using a regular dict with get()
    myMap3 = {}
    print(f"myMap3.get('x', 0): {myMap3.get('x', 0)}")  # 0

def find_consecutive_numbers(nums: List[int]) -> int:
    myMap = defaultdict(int)
    max_length = 0
    
    # First pass: count occurrences of each number
    for num in nums:
        myMap[num] += 1
    
    # Second pass: find consecutive sequences
    for num in nums:
        if num - 1 not in myMap:  # Only start from the smallest number in a sequence
            current_num = num
            current_length = 0
            
            # Count consecutive numbers
            while current_num in myMap:
                current_length += 1
                current_num += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def find_consecutive_numbers_original_approach(nums: List[int]) -> int:
    myMap = defaultdict(int)
    max_length = 0
    
    # First, add all numbers to the map
    for num in nums:
        myMap[num] = 1
    
    # Then check consecutive numbers
    for number in nums:
        cntUp = 1
        cntDown = 1
        current_length = 1  # Start with 1 for the current number
        
        # Check numbers above
        while number + cntUp in myMap:
            current_length += 1
            cntUp += 1
        
        # Check numbers below
        while number - cntDown in myMap:
            current_length += 1
            cntDown += 1
        
        max_length = max(max_length, current_length)
    
    return max_length

def longestConsecutive(nums: List[int]) -> int:
    mp = defaultdict(int)  # Map to store length of consecutive sequence for each number
    res = 0  # Track the maximum length found

    for num in nums:
        # Only process if we haven't seen this number before
        if not mp[num]:
            # Get the length of consecutive sequences on both sides
            # mp[num-1] gives length of sequence ending at num-1
            # mp[num+1] gives length of sequence starting at num+1
            # Add 1 for the current number
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            
            # Update the length at the start of the sequence
            # num - mp[num-1] is the start of the left sequence
            mp[num - mp[num - 1]] = mp[num]
            
            # Update the length at the end of the sequence
            # num + mp[num+1] is the end of the right sequence
            mp[num + mp[num + 1]] = mp[num]
            
            # Update the maximum length if needed
            res = max(res, mp[num])
    
    return res

arr = ["neet","code","love","you"]
arr2 = ["we","say",":","yes","!@#$%^&*()"]
print(decode(encode(arr)))
print(encode(arr))

print(encode2(arr2))

# Example usage
nums = [1, 2, 3, 4]
print(safe_division(nums))

# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Should output [24, 12, 8, 6]

# Example usage
test_nums1 = [1, 2, 3, 1]  # Has duplicate
test_nums2 = [1, 2, 3, 4]  # No duplicate
print(f"Using 'in' operator: {has_duplicate_using_in(test_nums1)}")  # True
print(f"Using len comparison: {has_duplicate_using_len(test_nums1)}")  # True
print(f"Using 'in' operator: {has_duplicate_using_in(test_nums2)}")  # False
print(f"Using len comparison: {has_duplicate_using_len(test_nums2)}")  # False

# Example usage
test_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(test_board))  # Should print True

# Run the examples
find_max_value_examples()

# Run the example
defaultdict_example()

# Example usage
test_nums = [100, 4, 200, 1, 3, 2]
print(f"Longest consecutive sequence length: {find_consecutive_numbers(test_nums)}")  # Should print 4

# Example usage
test_nums = [100, 4, 200, 1, 3, 2]
print(f"Original approach - Longest consecutive sequence length: {find_consecutive_numbers_original_approach(test_nums)}")  # Should print 4

# Example usage
test_nums = [100, 4, 200, 1, 3, 2]
print(f"Longest consecutive sequence length: {longestConsecutive(test_nums)}")  # Should print 4

# Example walkthrough:
# For nums = [100, 4, 200, 1, 3, 2]
# When processing 1:
#   - mp[1] = mp[0] + mp[2] + 1 = 0 + 0 + 1 = 1
#   - mp[1] = 1
# When processing 2:
#   - mp[2] = mp[1] + mp[3] + 1 = 1 + 0 + 1 = 2
#   - mp[1] = 2, mp[2] = 2
# When processing 3:
#   - mp[3] = mp[2] + mp[4] + 1 = 2 + 0 + 1 = 3
#   - mp[1] = 3, mp[3] = 3
# When processing 4:
#   - mp[4] = mp[3] + mp[5] + 1 = 3 + 0 + 1 = 4
#   - mp[1] = 4, mp[4] = 4