import math

def primes(N):
  sieve = set(range(2, N))

  for i in range(2, int(math.sqrt(N))):
    if i in sieve:
      sieve -= set(range(2*i, N, i))
  return sieve

p = list(primes(100000))

new_p = [] 
for i in p:
    new_p.append(p[i-1])
    #print(p[i-1])
    if len(new_p) == 500:
      break

#print(new_p)
print(new_p[int(input())-1])
