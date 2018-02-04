n = [int(i) for i in input().split()]

if n[1] < n[0] and n[0] < n[2]:
    print(n[0])
elif n[2] < n[0] and n[0] < n[1]:
    print(n[0])
    
elif n[2] < n[1] and n[1] < n[0]:
    print(n[1])
elif n[0] < n[1] and n[1] < n[2]:
    print(n[1])
    
elif n[1] < n[2] and n[2] < n[0]:
    print(n[2])    
elif n[0] < n[2] and n[2] < n[1]:
    print(n[2])
