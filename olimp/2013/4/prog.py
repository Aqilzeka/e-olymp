f = open("in.txt", "r").read().split(" ")
w = open('out.txt', 'w')
w.write(f[3] + ' ' + f[1] + ' ' + f[2] + ' ' + f[0])
w.close()
