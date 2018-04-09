import random

mass = [random.randint(-10,10) for i in range(20)]
output = []
for i in range(len(mass)):
    if mass[i] > mass[i - 1]:
        output.append(mass[i])

print(output)