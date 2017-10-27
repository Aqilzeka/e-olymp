f = open("in.txt", "r").read().split(" ")

a = int(f[0])
b = int(f[1])

c = 180 - (a + b)

if(a < 90) and (b < 90) and (c < 90):
    out = "Гострокутний"
elif(a == 90) or (b == 90) or (c == 90):
    out = "Прямокутний"
else:
    out = "Тупокутний"
    
w = open('out.txt', 'w')
w.write(out)
w.close()
