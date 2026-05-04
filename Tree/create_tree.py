def insert(node, value):
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
        
    return node

# Usage:
root = None
values = [10, 5, 15, 2, 7]
for val in values:
    root = insert(root, val)



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] is None:
        return None

    # The root is the first element
    root = Node(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        current = queue.pop(0)
        
        # Process left child: if null, we skip and leave as None (end of path)
        if i < len(values):
            if values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            
        # Process right child: if null, we skip and leave as None (end of path)
        if i < len(values):
            if values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1
            
    return root

# Example: [1, 2, 3, None, 5] 
# 1 is root, 2 is left, 3 is right. 2's left is null (end of path).
tree_root = build_tree([1, 2, 3, None, 5, 6, None])

