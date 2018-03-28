n = bin(int(input()))
count = 0
print(n)
for i in list(n):
    if i == "1":
        count += 1

print(count)