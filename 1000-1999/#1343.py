import itertools

r = open("input.txt", "r").read()
n = int(r)
mass = ["a", "b", "c"]
count = 0
for i in itertools.combinations_with_replacement(mass, n):
    temp = ""
    for j in i:
        temp += j
    print(temp)
    if temp.find("ab") == -1:
        count += 1
print(count)