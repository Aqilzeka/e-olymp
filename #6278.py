temp = input().split()
n = int(temp[0])
m = int(temp[1])
if (n % 2 == 0 and m % 2 == 0) or (n % 2 == 1 and m % 2 == 1):
 print(1)
else:
 print(0)