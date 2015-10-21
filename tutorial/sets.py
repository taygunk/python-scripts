# -*- coding: utf-8 -*-

# --------------- sets and operations --------------------------------------- #
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print('Intersection')
print(a.intersection(b))
print(b.intersection(a))

print('Symmetric diff')
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print('Diff')
print(a.difference(b))
print(b.difference(a))

print('Union')
print(a.union(b))
