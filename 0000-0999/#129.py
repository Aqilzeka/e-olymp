import math
R, ans = float(input()), 0
for i in range(1, int(R)):
    ans += sqrt(R * R - x * x)

ans *= 4
print(ans)