f = open("velo.in", "r").read().split("\n")
temp = f[0].split(" ")

N = int(temp[0])
M = int(temp[1])

spysok_dorig=[]
for i in range(1,M+1):
    temp = f[i].split(" ")
    doroga = [int(temp[0]),int(temp[1])]
    spysok_dorig.append(doroga)

print (spysok_dorig)
spysok_punktiv=[spysok_dorig[0][0],spysok_dorig[0][1]]
k=spysok_dorig[0][1]

for i in range(M):
    if spysok_punktiv.count(k)>1:
        spysok_punktiv=[spysok_dorig[i+1][0],spysok_dorig[i+1][1]]
        k=spysok_dorig[i+1][1]
    if spysok_punktiv.count(k)>1:
        spysok_punktiv=[spysok_dorig[i+1][0],spysok_dorig[i+1][1]]
        k=spysok_dorig[i+1][1]
    if (spysok_dorig[i][0]==k and len(spysok_punktiv)<N):
        spysok_punktiv.append(spysok_dorig[i][1])
        k=spysok_dorig[i][1]
        for j in range(M):
            if (spysok_dorig[j][0]==k and len(spysok_punktiv)<N):
                spysok_punktiv.append(spysok_dorig[j][1])
                k=spysok_dorig[j][1]                 
            
print (spysok_punktiv)
s=str()
for i in range(N):
     s = s+str(spysok_punktiv[i]) + ' '
w = open("velo.out", "w")
w.write(s)
w.close()
