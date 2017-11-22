# №3
N = int(input())
print(len([i for i in range(1,N+1) if not N % i]))

# №4
n = int(input())
s = 0
for i in range(n):
    s += int(input())
print(s)

# №5
a,b,c,d = int(input()),int(input()),int(input()),int(input())
r = ""
for i in range(1000):
    if (a*i*3 + b*i*2 + c*i + d) == 0:
        r += str(i) + " "

print(r)

# №6
n = int(input())
s = 0
for i in range(1,n+1):
    s += i

print(s)

# №7
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)
    
print(fib(int(input())))
