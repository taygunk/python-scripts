# --------------- for loops ------------------------------------------------- #
# -*- coding: utf-8 -*-

# Prints out the numbers 0,1,2,3,4
for x in xrange(5): # or range(5)
    print x

# Prints out 3,4,5
for x in xrange(3, 6): # or range(3, 6)
    print x

# Prints out 3,5,7
for x in xrange(3, 8, 2): # or range(3, 8, 2)
    print x

# Loop over list elems
# Prints "cat", "dog", "monkey", each on its own line.
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print animal

# Also access list indices
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)


    
# --------------- while loops ----------------------------------------------- #
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1

    
# --------------- "break" and "continue" statements ------------------------- #
# Prints out 0,1,2,3,4

count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x
    