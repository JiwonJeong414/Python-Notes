# If statements don't need parentheses
# or curly braces. just identation

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else :
    n += 2

# Parenthesis needed for multi-line conditions.
# and = &&
# or = ||
n, m = 1, 2
if((n > 2 and n != m) or n == m):
    n += 1

# While loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

# for loops
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

