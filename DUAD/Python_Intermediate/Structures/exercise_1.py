"""
Ejercicios de Estructuras de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 1 – Stack (LIFO – Last In, First Out)

Original requirement (translated):
- Create an object structure that resembles a Stack.
- It must include push (to add nodes) and pop (to remove nodes) methods.
- It must include a method to print the whole structure.
- You are NOT allowed to use composite data types like lists, dicts, or tuples,
  nor modules like collections.

Concept:
- A stack is a LIFO structure: the last element that goes in is the first one
  that comes out.
- We will implement it using nodes connected by references, similar to the
  LinkedList code from the notes (Node + LinkedList), but specialized as a Stack.
"""

# ------------------------------
# Node class
# ------------------------------


class Node:
 
    def __init__(self, data, next_node=None):
   
        self.data = data
        self.next = next_node


# ------------------------------
# Stack class
# ------------------------------


class Stack:

    def __init__(self, top=None):
    
        self.top = top

    def push(self, new_node):
        """
        Push a new node onto the top of the stack.

        Expected outcome:
            - The new node becomes the top of the stack.
            - The previous top moves one position down.
        """
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pop (remove) the top node from the stack and return it.

        Expected outcome:
            - The returned node is the one that was most recently pushed.
            - The stack becomes one element shorter.
        """
        if self.top is None:
            # Nothing to pop
            return None

        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None  # optional cleanup
        return popped_node

    def print_structure(self):
        """
        Print all nodes in the stack from top to bottom.

        Expected outcome:
            - The console shows the stack contents in order: top first,
              then each node below it.
        """
        current_node = self.top
        print("Stack contents (top to bottom):")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    # Create an empty stack.
    stack = Stack()

    # Push three nodes onto the stack.
    stack.push(Node("First element"))
    stack.push(Node("Second element"))
    stack.push(Node("Third element"))

    # Expected output:
    # Stack contents (top to bottom):
    # Third element
    # Second element
    # First element
    stack.print_structure()

    # Pop the top node.
    popped = stack.pop()
    # Expected:
    # popped.data == "Third element"
    print("Popped node:", popped.data if popped else None)

    # Print the stack again after popping.
    # Expected output:
    # Stack contents (top to bottom):
    # Second element
    # First element
    stack.print_structure()