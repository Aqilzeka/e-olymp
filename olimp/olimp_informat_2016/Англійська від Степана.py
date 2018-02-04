r = open("input.txt", "r").read().split("\n")
N = int(r[0])
mass = []

for i in range(N):
    mass.append(r[i + 1])



for i in range(N):
    temp = list(mass[i].lower())
    for j in range(len(temp)):
        

        
        if "s" == temp[j] and j != 0:
            if j + 1 == len(temp):
                    temp[j] = "th"
            elif "h" != temp[j + 1]:
                temp[j] = "th"
                
        if temp[0] == "e":
            temp[0] = "ae"
        if temp[j] == "o" and temp[j + 1] == "o":
            temp[j] = "o"
            temp[j + 1] = "u"

        
        
        temp_list = ""
        for j in range(len(temp)):
            temp_list += temp[j]
        mass[i] = temp_list

w = open("output.txt", "w")
for i in range(len(mass)):
    w.write(mass[i]+"\n")
w.close()
print(mass)
