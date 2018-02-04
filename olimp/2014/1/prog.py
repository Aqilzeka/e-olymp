f = open("in.txt", "r").read().split(" ")

l = int(f[0])
w = int(f[1])
h = int(f[2])
s = int(f[3])

b = round((l*w*h) / s)

w = open('out.txt', 'w')
w.write(str(b))
w.close()
