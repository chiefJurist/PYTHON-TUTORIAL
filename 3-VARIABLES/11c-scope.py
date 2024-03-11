# To create a global variable inside a function, you can use the global keyword.

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)