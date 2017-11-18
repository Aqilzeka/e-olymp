def sortByAlphabet(inputStr):
        return inputStr[0]

def sortByLength(inputStr):
        return len(inputStr)
    
        
sortList = ['a', 'cc', 'bbb']
sortList.sort(key=sortByAlphabet)
print(sortList)


sortList = ['a', 'cc', 'bbb']
sortList.sort(key=sortByLength)
print(sortList)


sortList = ['a', 'cc', 'bbb']
sortList.sort(key=sortByLength, reverse=True)
print(sortList)
