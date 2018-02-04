n = int(input())
sum = 0
for i in range(1,n):

    if sum + i*i < n:
        sum += i*i
    else:
        break
    print(i,'*',i)
    if sum == n or sum > n:
        break
print(sum)
