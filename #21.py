f = open("input.txt", "r").read().split("\n")
w = open('output.txt', 'w')
temp = f[0].split(" ")
N = int(temp[0])
P = float(temp[1]) / 100
G = [int(i) for i in f[1].split(" ")]

sum = (G[0]+G[1]) - (G[0]+G[1])*P

for i in range(1,N):
    sum = (sum + G[i]) - (sum + G[i])*P

print(sum)
    
