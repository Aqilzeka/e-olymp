h1 = {1:"one", 2:"two", 3:"three"}
h2 = {0:"zero", 5:"five"}
h3 = {"z":1, "y":2, "x":3}
d = {a: a ** 2 for a in range(7)}

for key, value in h1.items():
    print (key, " ", value)
print()
for key in h2.keys():
    print (key, " ", h2[key])
print()
for v in h3.values():
    print (v)
print()
for key, value in d.items():
    print (key, " ", value)
print()
