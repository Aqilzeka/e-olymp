f = open("in.txt", "r").read().split(" ")

n = int(f[0])
m = int(f[1])
k = int(f[2])
sum = 0

for i in range(n):
    sum += m
    m += k


w = open('out.txt', 'w')
w.write(str(sum))
w.close()
