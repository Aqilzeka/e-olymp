list1 = list(input())
list2 = list(input())

list1 = [list1[i-1]+list1[i] for i in range(len(list1))]
list1.pop(0)
list2 = [list2[i-1]+list2[i] for i in range(len(list2))]
list2.pop(0)
sum = 0
if len(list1) >= len(list2): 
    for i in range(len(list1)):
        if list1[i] in list2:
            sum += 1
else:
    for i in range(len(list2)):
        if list2[i] in list1:
            sum += 1

print(sum)
