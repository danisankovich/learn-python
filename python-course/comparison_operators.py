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
