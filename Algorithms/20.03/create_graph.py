n = int(input())
m = int(input())
mass = [[] for i in range(n)]

for i in range(n):
  temp = input().split()
  mass[int(temp[0]) - 1].append(int(temp[1]))
  mass[int(temp[1]) - 1].append(int(temp[0]))
  
print(mass)
