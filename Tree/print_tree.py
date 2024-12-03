# Import necessary functions to build a tree and use the BinaryTree class
from main import build_tree
from tree import BinaryTree

# Build the tree using the build_tree function
root_node = build_tree()
tree = BinaryTree(root_node)

def print_tree(root_node):
    """
    This function prints the structure of the binary tree in a visual representation.
    It prints each level of the tree and uses slashes and backslashes to represent the branches.
    :param root_node: The root node of the binary tree to print.
    """
    # Initialize an empty list to hold the nodes at each level of the tree
    tree_levels = []

    # Collect nodes for each level of the tree from height 0 to the maximum height
    for level in range(tree.height(root_node) + 1):
        tree_levels.append(tree.height_print(root_node, 0, level))

    # Print the structure of the tree, starting with the top level
    spacing = len(tree_levels) * 2  # Initial space between levels

    # Loop through each level in the tree_levels list
    for level_nodes in tree_levels:
        if len(level_nodes) != 1:
            count = 0  # Counter for branch printing
            # Loop through nodes in the current level
            for node in level_nodes:
                if node is None:
                    node = "_"  # Replace None with an underscore for clarity
                # Alternate between slashes and backslashes for branches
                if count % 2 == 0:
                    branch = "/"
                else:
                    branch = "\\"
                # Print the branch with the required spacing
                print(spacing * ' ', branch, end='')
                count += 1
        print()  # New line after printing branches
        # Print the actual node data (or dashes if None)
        for node in level_nodes:
            if node is None:
                node = "-"  # Replace None with a dash for clarity
            print(spacing * ' ', node, end='')

        print()  # New line after printing nodes
        spacing = int(spacing / 2)  # Reduce spacing for the next level

# Print the visual representation of the tree
print_tree(root_node)
