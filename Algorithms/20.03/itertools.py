import itertools
mass = [1,2,3]
n = len(mass)
for i in itertools.permutations(mass, n):
  print (i)
