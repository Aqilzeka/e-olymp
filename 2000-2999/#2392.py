n = list(input())

max = sorted(n, reverse=True)
max_int = ""
for i in max: max_int += i
max_int = int(max_int)
min = sorted(n, reverse=False)
min_int = ""
for i in min: min_int += i
min_int = int(min_int)

print(max_int + min_int)
