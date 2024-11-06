class Tree:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def search(self, root, target):
        if root is None:
            return
        if root.data == target:
            return f"Data Found: {root.data}"

        return self.search(root.left,5) or self.search(root.right, 5)
    
    def preorder(self, root):
        print(root.data)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)
        
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        print(root.data)
        if root.right:
            self.inorder(root.right)

    def postorder(self, root):
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        print(root.data)
    
    def height(self, root):
        if root.left is None and root.right is None:
            return 0
        l = self.height(root.left) + 1
        r = self.height(root.right) + 1
        return max(l, r)
    
    def height_print(self, root, initi, height, data=[]):
        if initi == height:
            data.append(root.data)

        try:
            self.height_print(root.left, initi+1, height)
        except:
            if initi == height or (initi+1 == height):
                data.extend([None])
        try:    
            self.height_print(root.right, initi+1, height)
        except:
            if initi == height or (initi+1 == height):
                data.extend([None])
        return data
            
    def print_tree(self, root):
        print()

node = Tree(7)
node.left = Tree(3)
node.right = Tree(9)
node.left.left = Tree(1)
node.left.right = Tree(5)
node.right.left = Tree(8)
node.right.right = Tree(10)
node.right.right.right = Tree(1090)

check = BinaryTree(node)

# Print the node values present in the same height
print("*******************************************")
print("Printing the same height nodes: ", check.height_print(node, 0, 2))

# Searching the specific node values present in the binary tree
# print(check.search(node, 5))

# Print the values in the preorder manner
# check.preorder(node)

# Print the values in the inorder manner
# print("*******************************************")
# check.inorder(node)

# Print the values in the postorder manner
# print("*******************************************")
# check.postorder(node)

# Print the height of the tree
# print("*******************************************")
# print(check.height(node))
