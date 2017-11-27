f = open("input.txt", "r").read().split("\n")
a,b,c,d = f[0].split(" "),f[1].split(" "),f[2].split(" "),f[3].split(" ")
A = []
A.append(int(a[0]))
A.append(int(a[1]))
A.append(int(b[0]))
A.append(int(b[1]))
A.append(int(c[0]))
A.append(int(c[1]))
A.append(int(d[0]))
A.append(int(d[1]))

print(A)

#w = open("output.txt", "w")

if (A[1]==A[3]) and (A[0]==A[4]) and (A[2]==A[6]) and (A[5]==A[7]):
    print("YES")
else:
    print('NO');
