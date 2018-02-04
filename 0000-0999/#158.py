def fib(n):
    if n==1 or n==2 or n==3 or n==4:
        return 1
    return fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4)

f = open("input.txt", "r").read().split("\n")
n = int(f[0])

mass = [int(i) for i in f[1].split()]

w = open("output.txt", "w")
for i in mass:
    w.write(str(fib(i))+"\n")
w.close()
