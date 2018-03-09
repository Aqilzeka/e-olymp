def function(i, j):
            count = 0 
            if i == 0 and j == 0:
                if mass[i + 1][j] == "#":
                    count += 1
                elif count_mass[i + 1][j] == -1:
                    function(i + 1, j)
        
                if mass[i][j + 1] == "#":
                    count += 1
                elif count_mass[i][j + 1] == -1:
                    function(i, j + 1)
                    
            elif i == n - 1 and j == n - 1:
                if mass[i - 1][j] == "#":
                    count += 1
                elif count_mass[i - 1][j] == -1:
                    function(i - 1, j)
                if mass[i][j - 1] == "#":
                    count += 1
                elif count_mass[i][j - 1] == -1:
                    function(i, j - 1)
                    
            elif i < n and j < n:
                if i == n - 1 or mass[i + 1][j] == "#":
                     count += 1
                     function(i + 1, j)
                if i == 0 or mass[i - 1][j] == "#":
                    count += 1
                    function(i - 1, j)

                if j == n - 1 or mass[i][j + 1] == "#":
                    count += 1
                    function(i, j + 1)
                if j == 0 or mass[i][j - 1] == "#":
                    count += 1
                    function(i, j - 1)
                     
                if mass[i + 1][j] == "#": count += 1
                if mass[i][j + 1] == "#": count += 1
                if mass[i - 1][j] == "#": count += 1
                if mass[i][j - 1] == "#": count += 1
            count_mass[i][j] = count
                    


r = open("input.txt", "r").read().split("\n")
n = int(r[0])

mass = []
count_mass = []

for i in range(n):
    temp = list(r[i + 1])
    mass.append([])
    count_mass.append([])
    for j in range(n):
            mass[i].append(temp[j])
            count_mass[i].append(-1)

for i in range(n):
    for j in range(n):
        print (mass[i][j], end = " ")
    print()
print()




function(0,0)
for i in range(n):
    for j in range(n):
        print(count_mass[i][j], end = " ")
    print()
