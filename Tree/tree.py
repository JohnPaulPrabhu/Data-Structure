# Importing the build_tree function from the main module to build the tree.
from main import build_tree


class BinaryTree:
    def __init__(self, root):
        """
        Initialize the binary tree with the root node.
        :param root: The root node of the binary tree.
        """
        self.root = root

    def search(self, root, target):
        """
        Search for a node with the given target value in the binary tree.
        :param root: The current node being examined.
        :param target: The value to search for.
        :return: A message indicating if the target is found or not.
        """
        # If the current node is None, return None (target not found).
        if root is None:
            return None
        
        # If the data at the current node matches the target, return a success message.
        if root.data == target:
            return f"Data Found: {root.data}"

        # Recursively search the left and right subtrees.
        return self.search(root.left, target) or self.search(root.right, target)
    
    def preorder(self, root):
        """
        Perform preorder traversal (root, left, right) on the binary tree.
        :param root: The current node being examined.
        """
        # Print the current node's data.
        print(root.data)
        
        # Recursively traverse the left subtree.
        if root.left:
            self.preorder(root.left)
        
        # Recursively traverse the right subtree.
        if root.right:
            self.preorder(root.right)
        
    def inorder(self, root):
        """
        Perform inorder traversal (left, root, right) on the binary tree.
        :param root: The current node being examined.
        """
        # Recursively traverse the left subtree.
        if root.left:
            self.inorder(root.left)
        
        # Print the current node's data.
        print(root.data)
        
        # Recursively traverse the right subtree.
        if root.right:
            self.inorder(root.right)

    def postorder(self, root):
        """
        Perform postorder traversal (left, right, root) on the binary tree.
        :param root: The current node being examined.
        """
        # Recursively traverse the left subtree.
        if root.left:
            self.postorder(root.left)
        
        # Recursively traverse the right subtree.
        if root.right:
            self.postorder(root.right)
        
        # Print the current node's data.
        print(root.data)
    
    def height(self, root):
        """
        Calculate the height of the binary tree.
        :param root: The current node being examined.
        :return: The height of the binary tree.
        """
        # If the current node is a leaf (both left and right are None), the height is 0.
        if root.left is None and root.right is None:
            return 0
        
        # Initialize height values for left and right subtrees.
        l = r = 0
        
        # Calculate the height of the left subtree if it exists.
        if root.left:
            l = self.height(root.left) + 1
        
        # Calculate the height of the right subtree if it exists.
        if root.right:    
            r = self.height(root.right) + 1
        
        # Return the maximum height between the left and right subtrees.
        return max(l, r)
    
    def height_print(self, root, initi, height, data=None):
        """
        Collect and return the node values at a specific height in the tree.
        :param root: The current node being examined.
        :param initi: The current level or depth of the node in the tree.
        :param height: The target level/depth where we want to collect the nodes.
        :param data: The list of nodes at the target height (accumulates results).
        :return: A list of nodes at the specified height.
        """
        # If the data list is not provided, initialize it as an empty list.
        if data is None:
            data = []
        
        # If the current node's level matches the target height, add its data to the list.
        if initi == height:
            data.append(root.data)

        # Recursively search the left and right subtrees, incrementing the level.
        try:
            self.height_print(root.left, initi + 1, height, data)
        except:
            # If an error occurs (e.g., reaching a None node), add None if necessary.
            if initi == height or (initi + 1 == height):
                data.extend([None])
        
        try:    
            self.height_print(root.right, initi + 1, height, data)
        except:
            # Similarly, add None for the right subtree if it reaches the target height.
            if initi == height or (initi + 1 == height):
                data.extend([None])

        # Return the accumulated data list.
        return data


# Build the binary tree using the build_tree function from the 'main' module.
node = build_tree()

# Create a BinaryTree object with the root node.
check = BinaryTree(node)

# Print the height of the tree.
print("Height of the tree is: ", check.height(node))

# Print the nodes at the 2nd, 3rd, and 4th heights.
print("Printing the same height nodes: ", check.height_print(node, 0, 2))
print("Printing the same height nodes: ", check.height_print(node, 0, 3))
print("Printing the same height nodes: ", check.height_print(node, 0, 4))
