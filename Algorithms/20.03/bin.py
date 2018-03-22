n = 9
for i in range(pow(2,n)):
    b = bin(i).replace("0b", "")
    add = (n - len(b)) * "0"
    print(add + b)