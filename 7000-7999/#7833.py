r = open("input.txt", "r").read().split("\n")
n = int(r[0])
mass = [int(i) for i in r[1].split(" ")]

summ,k = 0,0
s = sum(mass)/n
for i in range(n):
    if s < float(mass[i]):
        summ += mass[i]
        k += 1

w = open("output.txt", "w")

w.write(str(summ)+" "+str(k))

w.close()
