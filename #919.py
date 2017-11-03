f = open("input.txt", "r").read().split("\n")
n = int(f[0])

mas = f[1].split(" ")
line = ''
k = 0
template = '{:.2f}'

for i in range(n):
    if ((i+1) % 3 == 0) and float(mas[i]) > 0:
        line = line + template.format(float(mas[i])) + ' '
        k += 1
        
w = open("output.txt", "w")
w.write(str(k) + ' ' + line)
w.close()
