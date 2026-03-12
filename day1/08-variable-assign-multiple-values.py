# Python Variables - Assign Multiple Values

# Assign many values to multiple variables

# You can put several values on one line and assign them to several variables at once

# Example
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# Make sure the number of variables matches the number of values, or Python gives an error.

# Assign one value to multiple variables
# You can also assign the same value to multiple variables in one line.

# Example
q = w = e = "Orange"

print(q)
print(w)
print(e)

# Unpack a collection
# If you have a list, tuple, or other collection, you can extract its values into variables. This is called unpacking.

# Example
fruits = ["apple", "banana", "cherry"]
t, c, u = fruits

print(t)
print(c)
print(u)

# Python assigns "apple" -> t, "banana" -> c, "cherry" -> u.
