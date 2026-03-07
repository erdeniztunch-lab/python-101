# Python - Global Variables

# What is a global variable?
# a variable created outside a function is called a global variable.

# it can be used anywhere in the program, both inside and outside functions.

# Using a global variable inside a function

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Here "x" is global, so the function can use it.

# Output: Python is awesome.

# ----------------------------

# Local variables with the same name
# If you create a variable inside a function, it becomes local and only exists inside that function.

x = "awesome"


def myfunction():
    x = "Fantastic"
    print("Python is " + x)


myfunction()
print("Python is " + x)

# Output
# Python is fantastic
# Python is awesome

# Inside the function  -> x = "Fantastic"
# Outside the function -> x = "awesome"

# ----------------------------

# The global keyword
# Normally variables created in function are local.
# use global if you want to create or modify a global variable inside a function.


def myfuncti():
    global x
    x = "fantastic"


myfuncti()
print("Python is " + x)

# Output: "Python is fantastic"
