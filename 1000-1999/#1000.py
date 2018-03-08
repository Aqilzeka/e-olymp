f = open("input.txt", "r").readlines()
w = open('output.txt', 'w')

for i in range(len(f)):
  temp = f[i].split(" ")
  w.write(str(int(temp[0])+int(temp[1]))+"\n")


w.close()
