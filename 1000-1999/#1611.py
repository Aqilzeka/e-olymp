w = list(input())
temp = input().split()

i, j = int(temp[0]), int(temp[1])

w[i - 1], w[j - 1] = w[j - 1], w[i - 1]
str = ""
for i in w:
    str += i
print(str)
