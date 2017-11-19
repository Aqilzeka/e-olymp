a = int(input())

d = a/86400;
a = a%86400;
h = a/3600;
a = a%3600;
hv = a/60;
s = a%60;
print(int(d), int(h), int(hv), int(s))

