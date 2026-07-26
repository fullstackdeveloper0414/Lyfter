"""
Ejercicios de Estructuras de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 3 – Binary Tree

Original requirement (translated):
- Create an object structure that resembles a Binary Tree.
- It must include a method to print the whole structure.
- You are NOT allowed to use composite data types like lists, dicts, or tuples,
  nor modules like collections.

Concept:
- A binary tree is based on the idea of linked nodes, similar to Linked Lists,
  but each node can have up to two children: left and right.
- The structure has a root node at the top.
- We will implement a simple Binary Tree with a method to print all nodes
  using an in-order traversal (left, root, right).
"""

# ------------------------------
# Node class for Binary Tree
# ------------------------------


class TreeNode:
    
    def __init__(self, data, left=None, right=None):
      
        self.data = data
        self.left = left
        self.right = right


# ------------------------------
# Binary Tree class
# ------------------------------


class BinaryTree:
    
    def __init__(self, root=None):
      
        self.root = root

    def print_structure(self):
        """
        Print all nodes in the tree using in-order traversal.

        Expected outcome:
            - All nodes in the tree are printed to the console, one per line.
        """
        print("BinaryTree contents (in-order traversal):")
        self._print_in_order(self.root)

    def _print_in_order(self, node):
      
        if node is None:
            return

        # Visit left child.
        self._print_in_order(node.left)

        # Visit current node.
        print(node.data)

        # Visit right child.
        self._print_in_order(node.right)


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    # Construct a simple binary tree manually:
    #
    #        "B"
    #       /   \
    #     "A"   "C"
    #
    # In-order traversal should print: A, B, C

    node_a = TreeNode("A")
    node_c = TreeNode("C")
    root_b = TreeNode("B", left=node_a, right=node_c)

    tree = BinaryTree(root_b)

    # Expected output:
    # BinaryTree contents (in-order traversal):
    # A
    # B
    # C
    tree.print_structure()