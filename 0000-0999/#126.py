temp = input().split()
a, b, c, d, tmp, index = int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), int(temp[3]), 1

while tmp > a / b:
    tmp -= a / b
    index += 1

print(index, end=" ")
tmp, index = int(temp[3]), 1

while d > a / (b * c):
    d -= a / (b * c)
    index += 1
    if index == c + 1: index = 1

print(index)