def reverse(a):
    for i in range(len(a)//2):
        b = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = b
    return a
    

r = open("input.txt", "r").read().replace(",", " ").replace(":", " ").replace(";", " ").replace("/", " ").lower()
mass_sentence = r.split(".")
mass_sentence.pop(-1)

#print(mass_sentence)

mass = []
for i in range(len(mass_sentence)):
    mass.append([])
    for j in mass_sentence[i].split(" "):
        mass[i].append(j)
    mass[i] = [mass[i] for mass[i] in mass[i] if mass[i]]
    
counts_mass = []
for i in range(len(mass)):
    count = 0
    for j in range(len(mass[i])):

            if list(mass[i][j]) == reverse(list(mass[i][j])):
                #print(i,list(mass[i][j]),reverse(list(mass[i][j])))
                count += 1
    counts_mass.append(count)

w = open("output.txt", "w")
w.write(str(counts_mass.index(max(counts_mass))+1))
w.close()
#exit()
