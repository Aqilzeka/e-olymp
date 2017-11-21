n_str = input()
n = int(n_str)
s = 0

while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
    s += 1

print(s)
