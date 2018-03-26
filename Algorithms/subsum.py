def backtracking (tree, n, sub):
    if len(tree) == 0:
        tree.append(n)
        tree.insert(0, [])
        tree.insert(2, sub)
        tree.insert(3, [])

        #print(tree)
    else:
        for i in mass:
            temp = tree[1] + i
            sub = tree[2] + " " + str(i)
            if temp < sum:
                mass.pop(mass.index(i))
                backtracking(tree[0], temp, sub)
            else:
                temp = i
                sub = str(i)
                mass.pop(mass.index(i))
                backtracking(tree[3], temp, sub)




            #else:
            #    backtracking(tree[2], temp)
        '''
        elif temp < sum:
            backtracking(tree[2], temp)
        '''

tree = []
sum = 39
mass = [31,27,15,11,7,5]
backtracking(tree, 0, "")
for i in mass:
    backtracking(tree, i, "")


print(tree)
