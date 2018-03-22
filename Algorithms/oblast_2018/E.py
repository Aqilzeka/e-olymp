r = open("input.txt", "r").read().split()
n, c = int(r[0]), int(r[1])
count = 0
temp = (c + 1) * "1"
#print(temp)
for i in range(pow(2,n)):
    b = bin(i).replace("0b", "")
    add = (n - len(b)) * "0"
    b = add + b
    if not temp in b:
        count += 1
print(count)