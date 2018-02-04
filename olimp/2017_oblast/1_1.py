str1 = open("in.txt","r").read()
ah = "a"
ha = "ha"
sum = 0
for i in range(len(str1)):
    if ah in str1:
        sum = len(ah)
    elif ha in str1:
        sum = len(ha)
    if (i % 2) == 0:
        ah += "h"
        ha += "h"
    else:
        ah += "a"
        ha += "a"

print(sum)
        
        
