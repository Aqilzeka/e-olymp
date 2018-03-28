def function(n):
    E, AA, A, B = 0, 0, 0, 1
    for i in range(1, n):
        OE = E
        OAA = AA
        OA = A
        OB = B
        E = OE*2 + OAA
        AA = OA
        A = OB
        B = OAA + OA + OB
    return AA + A + B


n = int(input())
print(function(n))