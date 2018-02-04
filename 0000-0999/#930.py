mass = set([0,1,2,3,4,5,6,7,8,9])
f = open("input.txt", "r").read()
n = list(f)
n = set([int(i) for i in n])


n = n.symmetric_difference(mass)
n = sorted(n)
line = ''
for i in range(len(n)):
    if i == 0: line += str(i)
    else: line += " "+str(i)

w = open("output.txt", "w")
w.write(str(len(n)) + '\n' + line)
w.close()
