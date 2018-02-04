import math
def log(a):
    count = 0
    while a >= 1:
        a = round(a / 2)
        count += 1
    return count
    
r = open("input.txt", "r").read().split("\n")
n = int(r[0])
mass = []
for i in range(n):
    mass.append(int(r[i + 1]))
#print(len(mass))


w = open("output.txt", "w")
for i in range(len(mass)):
    w.write("Case #" + str(i + 1) + ": " + str(log(mass[i])) + "\n")
w.close()

