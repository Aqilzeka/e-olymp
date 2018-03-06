n = input().split()
n = n[0]+n[1]
n = list(n)
max = sorted(n, reverse=True)
max_int = ""
for i in max: max_int += i
max_int = int(max_int)

print(max_int)
