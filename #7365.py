f = open("input.txt", "r").read().split("\n")
o = open('output.txt', 'w')

n = int(f[0])
f = f[1].split(" ")
p = 0
m = 0.2
u = 0.9
for i in range(n):
    w = int(f[i])
    if (w<30):
        p += 1
    if(w>=30):
        p = p+0
    
k = round(p * m / u)

o.write(str(k)+" "+str(p))
o.close()
