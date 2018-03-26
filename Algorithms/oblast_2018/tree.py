class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def retur(self):
        return self
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


mass = [6,2,5,1,12,9,23]
function = Tree(mass[0])

for i in range(1,len(mass)):
    function.insert(mass[i])


print(function.retur())
function.PrintTree()