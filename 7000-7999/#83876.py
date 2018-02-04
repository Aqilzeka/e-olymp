n = int(input())
mass = [int(i) for i in input().split(" ")]
temp = ""
for i in range(n):
    if mass[i] % 2 == 1:
        temp += str(mass[i])+" "
print(temp)
