import random

mass = [random.randint(-10,10) for i in range(20)]

print(mass)
print(set(mass))

#or

import random

mass = [random.randint(-10,10) for i in range(20)]

output = []
for x in mass:
    if x not in output:
        output.append(x)

print(mass)
print(output)