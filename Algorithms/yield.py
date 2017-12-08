def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

mygenerator = createGenerator() # создаём генератор

for i in mygenerator:
     print(i)

for i in mygenerator:
     print(i)
