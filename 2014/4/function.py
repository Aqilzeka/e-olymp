def mag(f):
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
        return "No"
        break
    else:
        oldsum = sum
    sum = 0
 
 for i in range(n):
    for j in range(n):
        sum += mas[j][i]
        
    if oldsum == 0:
        oldsum = sum

    if(oldsum != sum):
        return "No"
        break
    else:

        oldsum = sum
    sum = 0
    
 for i in range(n):
    sum += mas[i][i]
	
 if(oldsum == sum):
    return "Yes"
 else:
    return "No"
