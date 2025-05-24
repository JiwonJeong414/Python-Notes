# Strings are similar to arrays
s = "abc"
print(s[0:2])

# But they are immutable (can't modifiy the string)
# s[0] = "A"

# So this creates a new string
s += "def"
print(s)

# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# # In rare cases you may need the ASCII value
# of a char
print(ord("a"))
print(ord("b"))

# Combine a list of stings(with an empty string)
# delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))

# String multiplication and concatenation
def string_times(str, n):
    string = ""  # Initialize as empty string, not None
    for i in range(n):
        string += str
    return string

# Or more simply, you can use string multiplication
def string_times_simple(str, n):
    return str * n

print(string_times("Hi", 3))        # "HiHiHi"
print(string_times_simple("Hi", 3))  # "HiHiHi"

# String search methods
text = "hixxxhi"
print(text.find("hi"))     # Returns 0 (first position of "hi")
print(text.find("hi", 1))  # Returns 5 (finds "hi" starting from position 1)
print(text.count("hi"))    # Returns 2 (counts all occurrences of "hi")

# String Slicing
# str[start:end] - gets characters from index start to end-1
# str[:end] - gets characters from start to end-1
# str[start:] - gets characters from start to end
# str[:] - gets all characters

text = "notebook"
print(text[:3])    # "not" - first 3 characters
print(text[3:])    # "ebook" - from index 3 to end
print(text[3:6])   # "ebo" - from index 3 to 5
print(text[:])     # "notebook" - all characters

# Getting specific characters
text = "Python"
print(text[0])     # "P" - first character
print(text[-1])    # "n" - last character
print(text[2])     # "t" - third character
print(text[-2])    # "o" - second to last character

# Common use case: checking prefixes
def add_not(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str

print(add_not("notebook"))  # "notebook"
print(add_not("hello"))     # "not hello"

# Negative indices
text = "Python"
print(text[-3:])   # "hon" - last 3 characters
print(text[:-3])   # "Pyt" - all except last 3 characters

# Step in slicing
text = "Python"
print(text[::2])   # "Pto" - every second character
print(text[::-1])  # "nohtyP" - reverse string

