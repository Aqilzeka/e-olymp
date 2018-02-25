temp = input().split()
a, c = int(temp[0]), int(temp[0])
b, flag = a, True
while flag:
    if a % c == 0:
        flag = False
    else:
        temp = list(str(b))
        lent = len(temp)
        mn = 1
        for j in range(lent):
            mn = mn * 10
            a = (a % c) * mn+b

print(a)
