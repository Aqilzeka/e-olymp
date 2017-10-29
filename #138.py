Q = [500, 200, 100, 50, 20, 10]

f = open("input.txt", "r").read().split("\n")
n = int(f[0])
x = 0
for i in range(6):
    q = Q[i]
    x += int(n / q)
    n = int(n % q)

if n > 0:
    x = -1

w = open("output.txt", "w")
w.write(str(x))
w.close()
