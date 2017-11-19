import datetime

a = input()
b = input()
a = a.split(' ')
b = b.split(' ')

aa = datetime.date(int(b[2]),int(b[1]),int(b[0]))
bb = datetime.date(int(a[2]),int(a[1]),int(a[0]))

cc = aa-bb
dd = str(cc)
print(dd.split()[0])
