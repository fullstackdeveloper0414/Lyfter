"""
Ejercicios de Estructuras de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 2 – Double Ended Queue (Deque)

Original requirement (translated):
- Create an object structure that resembles a Double Ended Queue.
- It must include:
    - push_left and push_right (to add nodes at the beginning and at the end).
    - pop_left and pop_right (to remove nodes at the beginning and at the end).
- It must include a method to print the whole structure.
- You are NOT allowed to use composite data types like lists, dicts, or tuples,
  nor modules like collections.

Concept:
- A double ended queue (deque) allows adding and removing elements from both
  the front (left) and the back (right).
- We will implement it using a doubly-linked list: each node has .next and .prev
  references, and the structure has both head and tail.
"""

# ------------------------------
# Node class for Deque
# ------------------------------


class DequeNode:

    def __init__(self, data, prev_node=None, next_node=None):
  
        self.data = data
        self.prev = prev_node
        self.next = next_node


# ------------------------------
# Double Ended Queue class
# ------------------------------


class DoubleEndedQueue:
    
    def __init__(self, head=None, tail=None):
        
        self.head = head
        self.tail = tail

    def push_left(self, new_node):
        """
        Insert a node at the left/front of the deque.

        Expected outcome:
            - new_node becomes the first element in the deque.
        """
        if self.head is None:
            # Deque is empty: new_node is both head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node in front of the current head.
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, new_node):
        """
        Insert a node at the right/back of the deque.

        Expected outcome:
            - new_node becomes the last element in the deque.
        """
        if self.tail is None:
            # Deque is empty: new_node is both head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        """
        Remove and return the node at the left/front of the deque.

        Expected outcome:
            - The returned node is the former leftmost node.
            - The deque has one fewer element.
        """
        if self.head is None:
            return None

        old_head = self.head
        new_head = old_head.next

        if new_head is None:
            # The deque had only one element.
            self.head = None
            self.tail = None
        else:
            new_head.prev = None
            self.head = new_head

        old_head.next = None
        old_head.prev = None
        return old_head

    def pop_right(self):
        """
        Remove and return the node at the right/back of the deque.

        Expected outcome:
            - The returned node is the former rightmost node.
            - The deque has one fewer element.
        """
        if self.tail is None:
            return None

        old_tail = self.tail
        new_tail = old_tail.prev

        if new_tail is None:
            # The deque had only one element.
            self.head = None
            self.tail = None
        else:
            new_tail.next = None
            self.tail = new_tail

        old_tail.prev = None
        old_tail.next = None
        return old_tail

    def print_structure(self):
        """
        Print all nodes in the deque from left (head) to right (tail).

        Expected outcome:
            - The console shows the deque contents from front to back.
        """
        current_node = self.head
        print("DoubleEndedQueue contents (left to right):")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    deque = DoubleEndedQueue()

    # Push elements from the right and left.
    deque.push_right(DequeNode("B"))
    deque.push_right(DequeNode("C"))
    deque.push_left(DequeNode("A"))

    # Expected output:
    # DoubleEndedQueue contents (left to right):
    # A
    # B
    # C
    deque.print_structure()

    # Pop from left.
    left_popped = deque.pop_left()
    print("Popped from left:", left_popped.data if left_popped else None)
    # Expected remaining contents:
    # B
    # C
    deque.print_structure()

    # Pop from right.
    right_popped = deque.pop_right()
    print("Popped from right:", right_popped.data if right_popped else None)
    # Expected remaining contents:
    # B
    deque.print_structure()