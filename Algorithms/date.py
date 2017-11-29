import time
import datetime
x = input().split(" ")
d, m, y = int(x[0]),int(x[1]),int(x[2])

date = str(d)+"/"+str(m)+"/"+str(y)

date = time.ctime(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())).split(" ")

date = date[0]

if date == "Mon":
    print("Понеділок")
elif date == "Tue":
    print("Вівторок")
elif date == "Wed":
    print("Середа")
elif date == "Thu":
    print("Четвер")
elif date == "Fri":
    print("П'ятниця")
elif date == "Sat":
    print("Субота")
elif date == "Sun":
    print("Неділя")
