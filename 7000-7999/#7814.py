import itertools

n = [int(i) for i in list(input())]

mass = itertools.combinations(n, 2)

str1 = ""
for i in min(mass):
    str1 += str(i)
print(str1)
