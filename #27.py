m = int(input())
s = bin(m)[2:]

for i in range(len(s) - 1):
    s = s[1:] + s[0]
    m = max(m, int(s, 2))
    
print (m)
