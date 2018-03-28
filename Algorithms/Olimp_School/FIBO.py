def fibo(x):
    if D[x] == 0:
        if 1 >= x <= 2:
            D[x] = 1
        else:
            D[x] = fibo(x - 1) + fibo(x - 2)
    return D[x]

D = [0 for i in range(50)]
n = int(input())
print(fibo(n))
