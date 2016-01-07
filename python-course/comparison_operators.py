x = 3
y = 4
z = 0
z += x
z -= y
print(z)

x == y # false
x != y # true
x > y # false
x < y # true
x >= y # false
x <= y # true

# Logical Operators: not, and, or

x = True
y = False
z = y or x # or |
print(z) # prints True => looks to see if either is true

x = True
y = False
z = y and x # or &
print(z) # prints false => looks to see if both are true

x = True
x = not x
print(x) # prints false

x = False
x = not x
print(x) # prints true

#===============================================================
#===============================================================
#===============================================================

c = [1, 2, 3]
a = [1, 2, 3]
b = a

# == checks equality, is checks identity => are things pointing at the same object
res_equality = (a == c)
print(res_equality) #true

res_is1 = (a is c)
print(res_is1) # false, because not pointing to same object.
print( a is b) # true, a and b pointed to same object
print( a is c) # false, a and c equal, but pointing to different object
print( a is not b) #false => they do point to the same place.

# by saying b = a, you say that b points to the same object that a points to, so
# a is b is true. b is c is false, because even though they are equal, it is pointing
# to a different object
