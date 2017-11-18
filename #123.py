def zero(d):
    i5 = d // 5
    x = i5
    while i5 > 0:
        i5 /= 5
        x += int(i5)

    return x
    
print (zero(int(input())))
