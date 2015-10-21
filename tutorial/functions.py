# -*- coding: utf-8 -*-
# --------------- function definition and calling---------------------------- #

def my_function():
    print "Hello From My Function!"

def my_function_with_args(username, greeting):
    print "Hello, %s , From My Function!, I wish you %s"%(username, greeting)
    
# print a simple greeting 
my_function()
#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")


# --------------- functions with varying number of parameters --------------- #
def foo(first, second, third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)
    
foo(1,2,3,4,5)     


# --------------- use keyword arguments in parameters ----------------------- #
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result

# --------------- functions with default parameters ------------------------- #
def hello(name, loud=False):
    if loud:
        print 'HELLO, %s' % name.upper()
    else:
        print 'Hello, %s!' % name

hello('Bob') # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"