temp = input().split()

t1, t2, t3 = int(temp[0]), int(temp[1]), int(temp[2])

t = float((1 / (1 / t1 + 1 / t2 + 1 / t3)))

print("{0:.2f}".format(t))
