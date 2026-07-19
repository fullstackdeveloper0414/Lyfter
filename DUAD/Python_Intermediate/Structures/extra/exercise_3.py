"""
Ejercicios Extra de Estructura de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 3 – Doubly Linked List

Original requirement (translated):
- Each node must have a reference to both the next and the previous node.
- Methods:
    - append(data): add at the end.
    - prepend(data): add at the beginning.
    - delete(data): remove the first node with that value.
    - print_forward(): print from head to tail.
    - print_backward(): print from tail to head.
- Restriction: do NOT use list, dict, tuple, or collections.

Behavior examples:
    dll.append("A")
    dll.append("B")
    dll.append("C")
    # print_forward  -> A -> B -> C
    # print_backward -> C -> B -> A

    dll.prepend("X")
    # print_forward  -> X -> A -> B -> C
    # print_backward -> C -> B -> A -> X

    dll.delete("B")
    # print_forward  -> X -> A -> C
    # print_backward -> C -> A -> X
"""

# ------------------------------
# Node class for Doubly Linked List
# ------------------------------


class DoublyNode:

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


# ------------------------------
# Doubly Linked List class
# ------------------------------


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Add a new node at the end of the list.
  
        Expected outcome:
            - The new node is added to the end.
            - Example:
                dll.append("A")
                dll.append("B")
                dll.append("C")
              Forward:  A -> B -> C
              Backward: C -> B -> A
        """
        new_node = DoublyNode(data)

        if self.tail is None:
            # List is empty.
            self.head = new_node
            self.tail = new_node
        else:
            # Link to end.
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """
        Add a new node at the beginning of the list.

        Expected outcome:
            - The new node is added to the front.
            - Example:
                Starting: A -> B -> C
                dll.prepend("X")
              Forward:  X -> A -> B -> C
              Backward: C -> B -> A -> X
        """
        new_node = DoublyNode(data)

        if self.head is None:
            # List is empty.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        """
        Delete the first node whose data matches the argument.

        Expected outcome:
            - The first match is removed, if present.
            - Examples:
                Before:  X -> A -> B -> C
                dll.delete("B")
              After:   X -> A -> C
        """
        current = self.head

        while current is not None:
            if current.data == data:
                # Case 1: only node in the list.
                if current is self.head and current is self.tail:
                    self.head = None
                    self.tail = None

                # Case 2: current is head, but not only node.
                elif current is self.head:
                    self.head = current.next
                    self.head.prev = None

                # Case 3: current is tail, but not only node.
                elif current is self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Case 4: middle node.
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                # Disconnect current node from list.
                current.prev = None
                current.next = None
                return  # stop after removing first match

            current = current.next
        # If we reach here, no node with that data was found.

    def print_forward(self):
        """
        Print all nodes from head to tail.

        Expected outcome:
            - The values appear from first to last.
        """
        current = self.head
        parts = []

        while current is not None:
            if parts:
                parts.append(" -> ")
            parts.append(str(current.data))
            current = current.next

        print("".join(parts))

    def print_backward(self):
        """
        Print all nodes from tail to head.

        Expected outcome:
            - The values appear from last to first.
        """
        current = self.tail
        parts = []

        while current is not None:
            if parts:
                parts.append(" -> ")
            parts.append(str(current.data))
            current = current.prev

        print("".join(parts))


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append("A")
    dll.append("B")
    dll.append("C")

    # Expected:
    # print_forward:  A -> B -> C
    # print_backward: C -> B -> A
    dll.print_forward()
    dll.print_backward()

    dll.prepend("X")
    # Expected:
    # print_forward:  X -> A -> B -> C
    # print_backward: C -> B -> A -> X
    dll.print_forward()
    dll.print_backward()

    dll.delete("B")
    # Expected:
    # print_forward:  X -> A -> C
    # print_backward: C -> A -> X
    dll.print_forward()
    dll.print_backward()