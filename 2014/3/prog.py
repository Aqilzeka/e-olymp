f = open("in.txt", "r").readlines()
n = int(f[0])
m = 1
sum = 0

for i in range(n):
    sum += m
    m += 2

w = open('out.txt', 'w')
w.write(str(sum))
w.close()
