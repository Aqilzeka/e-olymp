n = int(input())
i = 1
s = 0
while s <= n:

    s += i
    i += i*2
    if i > 100: break

print(s)
