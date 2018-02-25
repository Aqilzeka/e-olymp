str_in = input()
flag = True
n, temp_n, i = 2, 2, 2

while flag:
    if str(temp_n) in str_in:
        i += 1
        temp_n = pow(n, i)
    else:
        flag = False

print(i - 1)
