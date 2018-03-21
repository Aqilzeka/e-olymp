import collections

lst = [i for i in range(1, int(input()) + 1)]
k = int(input())
deq = collections.deque(enumerate(lst))

while len(deq) > 1:
     deq.rotate(-k)
     print(deq.pop()[1])

print(deq[0][1])
