# -*- coding: utf-8 -*-
# --------------- class definition ------------------------------------------ #

class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."

class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

# --------------- member access, function call ------------------------------ #
#first class
myobjectx = MyClass()
myobjectx.variable = "yackity"
print myobjectx.variable
myobjectx.function()

#second class
g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"

