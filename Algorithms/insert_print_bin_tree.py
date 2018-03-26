def insert (tree, n):
    if len(tree) == 0:
        tree.append(n)
        tree.insert(0,[])
        tree.insert(2,[])
        #print(tree)
    else:
        if tree[1] >= n:
            insert(tree[0], n)
        else:
            insert(tree[2], n)

def print_tree(tree):
    if tree != []:
        print_tree(tree[0])
        print(tree[1])
        print_tree(tree[2])

tree = []
mass = [6,3,7,4]
for i in mass:
    insert(tree, i)

print_tree(tree)
#print(tree)
