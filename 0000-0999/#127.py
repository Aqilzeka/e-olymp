n = int(input())
i = 1
s = 0
while s <= n:
    s += i*i
    i += i*i
    if i > 100: break

print(s)
