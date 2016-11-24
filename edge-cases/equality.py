from __future__ import print_function
# Q: Is it possible for 'x == x' to ever evaluate to False?
# A: Yes
x = float('nan') # Nan is not a number
x = 0 * float('inf') # also evaluates to nan
y = 0*1e309
print(x==x) # False
print(y==y) # False
