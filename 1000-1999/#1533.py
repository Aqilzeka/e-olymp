import itertools

r = open("input.txt", "r").read().split("\n")
n = int(r[0])


for i in range(1,n + 1):

    mass = list(r[i])
    n = len(mass)
    for i in itertools.permutations(mass, n):
        print(i)
