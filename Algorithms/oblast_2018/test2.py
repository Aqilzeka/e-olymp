globals(tree)
def insert(tree, n):
    if len(tree) == 0:
        tree = [[],n,[]]
    else:
        if tree[1] >= n:
            return insert(tree[0], n)
        else:
            return insert(tree[2], n)

mass = [7,2,3,5]
insert([],6)
for i in mass:
    insert(tree, i)