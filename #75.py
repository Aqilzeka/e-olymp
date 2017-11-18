a = int(input())
m = int(input())
s1, s, k, s2 = 0, 0, 0, 0
while m > 0:
    s1 = a + s
    k += 1
    s2 += s1
    if (m-s2==(s1+1)*2):
        break;
    else:
        s+=1
print(k + 1)
