# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: Fibonacci Numbers


# setting up variables (first two #s)
n1 = 0
n2 = 1
print(n1)
print(n2)

# for looping!
for i in range(2, 26):
    next = n1 + n2  # essentially, the formula for fibonacci sequence!
    print(next)
    
    n1 = n2         # so the numbers will be sequential and not 
    n2 = next       # stuck on just one number...
    
