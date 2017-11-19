d = input().split(" ")
a, b, n = float(d[0]),float(d[1]),int(d[2])

c = a+(b/100)
c = c*n
a = int(c)
b = round((c - int(c)) * 100)
print(a, b)

