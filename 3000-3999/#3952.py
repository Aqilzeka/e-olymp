import collections

r = open("input.txt", "r").read().split(" ")
w = open("output.txt", "w")
n, k = int(r[0]), int(r[1])
str_zero = "0"
point = 0
mass = []
for i in range(1, 100):
    #print(len(bin(i).replace("0b", "")))
    #if(len(bin(i).replace("0b", "")) == n):
    print(i, end=" ")
    bin1 = bin(i).replace("0b", "")

    count_one = collections.Counter(bin1)['1']
    if count_one == k:
        if len(bin1) < n:
            mass.append(str_zero*(n - len(bin1))+bin1)
            #w.write(str_zero*(n - len(bin1))+bin1)
        elif len(bin1) > n:
            break
        else:
            mass.append(bin1)
        #w.write("\n")

for i in range(len(mass)):
    if i == 0:
        w.write(mass[i])
    else:
        w.write("\n" + mass[i])



w.close()
    #break