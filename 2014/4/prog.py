from function import mag 

f = open("in.txt", "r").readlines()
w = open('out.txt', 'w')
w.write(mag(f))
w.close()

