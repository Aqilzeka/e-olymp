import collections
n = list(input())
a = str(input())
c = collections.Counter(n)
print(c[a])
