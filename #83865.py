r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
n = int(r[0])
for i in range(n):
    temp = r[i + 1].split(" ")
    w.write(str(int(temp[0]) + int(temp[1]))+"\n")

w.close()
