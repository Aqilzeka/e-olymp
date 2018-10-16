import collections

r = open("input.txt", "r").read().split(" ")
n, k = int(r[0]), int(r[1])

for i in range(1, 100):
    #print(len(bin(i).replace("0b", "")))
    #if(len(bin(i).replace("0b", "")) == n):
    print(i, end=" ")
    print(collections.Counter(bin(i).replace("0b", ""))['1'])
    #break