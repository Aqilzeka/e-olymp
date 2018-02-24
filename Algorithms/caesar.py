
alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя1234567890"
abc = list(alphabet)

def line():
    print("----------------------------------")

def caesar_crypt(str, n):
    list_in = list(str)
    out = ""
    for i in list_in:
        if i in abc:
            out += abc[(abc.index(i) + n) % len(abc)]
        else:
            out += i
    return out

def caesar_decrypt(str, n):

    list_in = list(str)
    out = ""
    for i in list_in:
        if i in abc:
            out += abc[(abc.index(i) - n) % len(abc)]
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

    key = int(input("enter decrypt key from 1 to " + len(abc).__str__() + ": "))

    return caesar_decrypt(str, key)



print("encrypt/decrypt alphabet:", alphabet)
print("[1] - encrypt text")
print("[2] - decrypt text")
print("[3] - crack encryption")
command = input("select action: ")

if command not in ['1', '2', '3']:
    print("wrong action")
    exit()
elif command == '1':
    filename = input("enter a file name: ")
    key = int(input("enter encrypt key from 1 to " + len(abc).__str__() + ": "))
    file = open(filename, "r").read().lower()

    line()
    print("encrypted text")
    print(caesar_crypt(file, key))
    line()

elif command == '2':
    filename = input("enter a file name: ")
    key = int(input("enter decrypt key from 1 to " + len(abc).__str__() + ": "))
    file = open(filename, "r").read().lower()

    line()
    print("decrypted text")
    print(caesar_decrypt(file, key))
    line()

elif command == '3':
    filename = input("enter a file name: ")

    file = open(filename, "r").read().lower()
    decrypted = caesar_hack(file)

    line()
    print("decrypted text")
    print(decrypted)
    line()

