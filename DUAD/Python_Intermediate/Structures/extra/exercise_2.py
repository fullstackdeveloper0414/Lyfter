"""
Ejercicios Extra de Estructura de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 2 – Singly LinkedList

Original requirement (translated):
- Create a class LinkedList with methods:
    - insert_front(data): insert at the beginning.
    - insert_back(data): insert at the end.
    - delete(data): delete the first node with the given value.
    - print_all(): print all values.

Behavior examples:
    ll.insert_front(10)
    ll.insert_front(20)
    # print_all -> 20 -> 10

    ll.insert_back(30)
    # print_all -> 20 -> 10 -> 30

    ll.delete(10)
    # print_all -> 20 -> 30
"""

# ------------------------------
# Node class for LinkedList
# ------------------------------


class ListNode:
    """
    Represents a single node in the singly linked list.

    Attributes:
        data: Value stored in this node.
        next: Reference to the next node in the list (or None if last).
    """

    def __init__(self, data, next_node=None):
    
        self.data = data
        self.next = next_node


# ------------------------------
# LinkedList class
# ------------------------------


class LinkedList:

    def __init__(self):
    
        self.head = None

    def insert_front(self, data):
        """
        Insert a new node at the beginning of the list.

        Expected outcome:
            - The new element appears at the front.
            - Example:
                ll.insert_front(10)
                ll.insert_front(20)
              List: 20 -> 10
        """
        new_node = ListNode(data, next_node=self.head)
        self.head = new_node

    def insert_back(self, data):
        """
        Insert a new node at the end of the list.

        Expected outcome:
            - The new element appears at the end.
            - Example:
                Starting: 20 -> 10
                ll.insert_back(30)
              List: 20 -> 10 -> 30
        """
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, data):
        """
        Delete the first node that has the given data value.

        Expected outcome:
            - The first matching node is removed if it exists.
            - Example:
                Starting: 20 -> 10 -> 30
                ll.delete(10)
              Result: 20 -> 30
        """
        if self.head is None:
            return

        # Check if the head node contains the value.
        if self.head.data == data:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            return

        # Traverse to find the value.
        prev = self.head
        current = self.head.next

        while current is not None:
            if current.data == data:
                # Bypass the current node.
                prev.next = current.next
                current.next = None
                return
            prev = current
            current = current.next

        # If we reach here, the value was not found; no change.

    def print_all(self):
        """
        Print all values in the list from head to end.

        Expected outcome:
            - The list contents appear in order.
        """
        current = self.head
        parts = []

        while current is not None:
            if parts:
                parts.append(" -> ")
            parts.append(str(current.data))
            current = current.next

        print("".join(parts))


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert at front.
    ll.insert_front(10)
    ll.insert_front(20)
    # Expected: 20 -> 10
    ll.print_all()

    # Insert at back.
    ll.insert_back(30)
    # Expected: 20 -> 10 -> 30
    ll.print_all()

    # Delete first node with value 10.
    ll.delete(10)
    # Expected: 20 -> 30
    ll.print_all()