class Tree:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

def build_tree():
    node = Tree(7)
    node.left = Tree(3)
    node.right = Tree(9)
    node.left.left = Tree(1)
    node.left.right = Tree(5)
    node.right.left = Tree(8)
    node.right.right = Tree(10)
    node.right.right.right = Tree(1090)
    return node

# check = BinaryTree(node)