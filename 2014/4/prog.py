f = open("in.txt", "r").readlines()
n = int(f[0])
mas = []
sum = 0
oldsum = 0

for i in range(n):
 mas.append([])
 l = f[i + 1].split(" ")
 for j in range(n):
   mas[i].append(int(l[j]))

for i in range(n):
    for j in range(n):
        sum += mas[i][j]
        
    if oldsum == 0:
            oldsum = sum
            
    if(sum != oldsum):
        out = "No"
        break
    else:
        out = "Yes"
        oldsum = sum
    sum = 0
 
for i in range(n):
    for j in range(n):
        sum += mas[j][i]
        
    if oldsum == 0:
        oldsum = sum

    if(oldsum != sum):
        out = "No"
        break
    else:
        out = "Yes"
        oldsum = sum
    sum = 0
    
for i in range(n):
	sum += mas[i][i]
	
if(oldsum == sum):
    out = "Yes"
else:
    out = "No"


w = open('out.txt', 'w')
w.write(out)
w.close()
