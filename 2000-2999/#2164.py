w = list(input())
n = int(input())

mass = ['A','B','C','D','E','F','G','H','I','J','K',\
        'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str = ""
for i in w:
    str += mass[mass.index(i) - n]

print(str)
