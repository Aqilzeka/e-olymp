list = [i for i in range(10)]
remove = int(input())
try:
    list.remove(remove)
except ValueError:
    list.pop()
finally:  
    print(list)
