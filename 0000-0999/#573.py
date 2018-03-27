n = int(input())
i = 1
flag = "no"

while i < pow(n, 10):
    if i % n == 0:
        #print()
        flag = bin(pow(2,i) - 1).replace("0b", "")
        break
    i += 1

print(flag)
exit()
for i in range(0,pow(n, 1000), pow(n, 2) - 1):
    print(bin(i))
