n = int(input())

s = [0 for i in range(100)]

s[1] = 1
s[2] = 2
s[3] = 4
if n > 3:
  for i in range(4,n+1):
    s[i] = s[i - 1] + s[i - 2] +s[i - 3]

print(s[n])
