# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuples are immutable if you try to change value in tuple you will get error
# my_tuple[1] = 5
# Traceback (most recent call last):
#   File "E:\python_practice\python_prep\module_2\tuples.py", line 12, in <module>
#     my_tuple[1] = 5
# TypeError: 'tuple' object does not support item assignment


# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


# Tuple with single value
# We will need a trailing comma to indicate that it is a tuple,

var1 = ("Hello") # string
var2 = ("Hello",) # tuple

# Methods

# Find index from the value of tuple
t1 = (10,20,20,30)
print(t1.index(20)) #=> 1

print(t1.count(20)) #=> 2

