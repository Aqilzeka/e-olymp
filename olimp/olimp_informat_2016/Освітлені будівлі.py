r = open("input.txt", "r").read().split("\n")
N = int(r[0])
H = [int(i) for i in r[1].split(" ")]

temp = H[0]
sum_h = 1
for i in range(1,N):
    if temp < H[i]:
        temp = H[i]
        sum_h += 1 

print(sum_h)
