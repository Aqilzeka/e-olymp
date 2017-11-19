def bin(a):
    if(a==1): return 2;
    if(a==2): return 4;
    return bin(a-1)+bin(a-2); 

print(bin(int(input())))
