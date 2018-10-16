r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
fib1, fib2 = 1, 1
fib = [0 for i in range(1001)]
fib[1] = 1
fib[2] = 1
n = 1000

i = 2
while i < n:
    fib[i + 1] = fib2 + fib1
    fib1 = fib[i]
    fib2 = fib[i + 1]
    i += 1

w.write(str(fib[int(r[0])]))
for i in range(1, len(r)):
    w.write("\n")
    w.write(str(fib[int(r[i])]))
