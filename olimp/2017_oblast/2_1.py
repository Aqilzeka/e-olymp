def new_mass(mass):
    new = []
    nomer = 0
    print(mass)
    if len(mass) >= 2:
        for i in mass:
            nomer += 1
            if nomer % 2 == 0:
                new.append(i)
        return new_mass(new)
    else:
        return mass

n = int(input())
mass = []
for i in range(1, n + 1):
    if i % 2 == 0:
        mass.append(i)

print(new_mass(mass))

