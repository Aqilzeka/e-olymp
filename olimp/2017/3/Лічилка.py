r = open("input.txt","r").read().split("\n")
temp = r[1].split(" ")
n, p, i = int(temp[0]), int(temp[1]), 0
k = len(r[0].split(" "))
print(n,p,k)
start = p
mass = [i for i in range(1,n + 1)]
while len(mass) >= 1:
    i += 1
    print(i,mass, start)
    if start + k >= len(mass):
        print("if",start + k,  len(mass) + 1)
        dell = int(((start + k) % len(mass)))
        print(dell)
        mass.pop(dell)
        start = ((start + k) % len(mass))
    else:
        print("else",start + k)
        mass.pop((start + k))
        start = ((start + k))
    
        
        

