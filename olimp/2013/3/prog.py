f = open("in.txt", "r")
f = f.readlines()
n = int(f[0])
sum = 0
for i in f[1].split(" "):
    if(int(i) % 2) == 0:
        sum += int(i)

w = open('out.txt', 'w')
w.write(str(sum))
w.close()
