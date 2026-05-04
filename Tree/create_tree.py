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
