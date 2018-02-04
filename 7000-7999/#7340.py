char = list(input())

result = {i: char.count(i) for i in char}

print(len(result))
