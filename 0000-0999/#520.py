r = open("input.txt", "r").read()
s = r
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
 
print(integ)

exit()
w = open("output.txt", "w")

w.write(str(sum(mass)))

w.close()
