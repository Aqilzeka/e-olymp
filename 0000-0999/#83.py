s = str(input()).split("/")
s[0],s[1],s[2] = str(bin(int(s[0]))), str(bin(int(s[1]))), str(bin(int(s[2])))
print(s[0].replace("0b", "")+"/"+s[1].replace("0b", "")+"/"+s[2].replace("0b", ""))
