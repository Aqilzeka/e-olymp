r = open("input.txt", "r").read().split("\n")
temp = r[0].split(" ")
N, X = int(temp[0]), int(temp[1])
A = [int(i) for i in r[1].split(" ")]

temp_mass = []
print(N,X,A)

for i in range(N):
    for j in range(N):
        if (A[i] + A[j]) <= X and i != j:
            temp_mass.append(A[i] + A[j])
            #print(A[i] + A[j])

print(max(temp_mass))

