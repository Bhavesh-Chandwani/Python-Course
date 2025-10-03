a = {1,2,3}
b = {3,4,5}

#Union of sets
c = a|b
print(f"The union of 2 sets are {c}")
#print(a.union(b)) Alternate method

#Intersection of sets
d = a&b
print(f"The intersection of 2 sets are {d}")

#difference of sets
e = a-b
f = b-a
print(f"The difference of set a and b {e}")
print(f"The difference of set b and a {f}")

#Symmetric differecne (^ or .symmetricdifference())
g = a ^ b
print(f"The symmetric difference between a an b is {g}")

#Subset and Superset
x = {1,2}
y = {1,2,3}
z = x <= y
a = y >= x
print(f"The x is subset of y {z}")
print(f"The y is superset of x {a}")

#Disjoint sets
p = {1,2,3}
q = {4,5,6}
c = p.isdisjoint(q)
print(f"The disjoint of a and b is {c}")