class TreeNode:
    def __init__(self, data) -> None:
        """
        Initialize a tree node with data and set left and right children to None.
        :param data: The value to store in this node.
        """
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node
        self.data = data  # Value stored in this node

def build_tree():
    """
    Build and return a sample binary tree.
    The tree structure is:
          7
         / \
        3   9
       / \  / \
      1   5 8  10
                   \
                   1090
    :return: The root node of the tree.
    """
    # Create the root node
    root_node = TreeNode(7)
    
    # Create left and right subtrees for the root
    root_node.left = TreeNode(3)
    root_node.right = TreeNode(9)
    
    # Create left and right children for the left subtree
    root_node.left.left = TreeNode(1)
    root_node.left.right = TreeNode(5)
    
    # Create left and right children for the right subtree
    root_node.right.left = TreeNode(8)
    root_node.right.right = TreeNode(10)
    
    # Add a right child to the right subtree
    root_node.right.right.right = TreeNode(1090)
    
    # Return the root node of the tree
    return root_node
