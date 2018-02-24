abc = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя1234567890")
global str

def caesar_decrypt(str, n):

    list_in = list(str)
    out = ""
    for i in list_in:
        if i in abc:
            out += abc[(abc.index(i) - n) % len(abc)]
        else:
            out += i
    return out

def caesar_crypt(str, n):

    list_in = list(str)
    out = ""
    for i in list_in:
        if i in abc:
            out += abc[(abc.index(i) + n) % len(abc)]
        else:
            out += i
    return out

def caesar_hack(str):
    list_in = str.split(" ")
    list_in.sort(key=len, reverse=True)
    max_len = list_in[0]
    count = 0
    for i in range(1,len(abc)):
        out = ""
        for j in max_len:
            if j in abc:
                out += abc[(abc.index(j) - i) % len(abc)]
            else:
                out += j
        if i < 10:
            i_print = i.__str__() + " "
        else:
            i_print = i.__str__()

        if count < 4:
            print("     ", end="")

            print("key =",i_print,"-",out, end="")
            count += 1
        elif count == 4:
            count = 0
            print("key =", i_print, "-", out)
    print("")

    key = int(input("decrypt key - "))

    return caesar_decrypt(str, key)


r = open("input.txt", "r").read().lower()
#w = open("output.txt", "w")
key = 2
crypt = caesar_crypt(r,key)
print(crypt)
decrypt = caesar_decrypt(crypt,key)
print(decrypt)
print(caesar_hack(crypt))
    #w.write(ROT(temp[1], int(temp[0]))+"\n")

#w.close()