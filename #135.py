def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)
  
r = open("input.txt", "r").read().split("\n")
n = int(r[0])
m = []
for i in r[1].split(" "):
    m.append(int(i))

#print(n)
#print(m)

for i in range(n):
    for j in range(i + 1, n):
        temp = gcd(m[i], m[j])
        m[j] /= temp
        
res = 1        
for i in range(n):
    res = res * m[i]

w = open("output.txt", "w")
w.write(str(int(res)))
w.close()
