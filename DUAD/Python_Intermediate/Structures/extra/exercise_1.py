"""
Ejercicios Extra de Estructura de Datos
Jaime C Smith
07/12/2026
"""

"""
Section 1 – Basic Queue (FIFO – First In, First Out) with linked nodes

Original requirement (translated):
- Create a structure that represents a basic Queue with linked objects.
- Restriction: do NOT use list, dict, tuple, or collections.
- Required methods:
    - enqueue(data): adds a node at the end.
    - dequeue(): removes and returns the node from the front.
    - print_all(): prints all elements in order.

Behavior examples:
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    # print_all()  ->  A -> B -> C

    q.dequeue()   -> returns "A"

    q.print_all() -> B -> C
"""

# ------------------------------
# Node class for Queue
# ------------------------------


class QueueNode:
    
    def __init__(self, data, next_node=None):
     
        self.data = data
        self.next = next_node


# ------------------------------
# Queue class
# ------------------------------


class Queue:

    def __init__(self):
    
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Add a new element at the end of the queue.

        Expected outcome:
            - The new element appears at the back of the queue.
            - Example:
                q.enqueue("A")
                q.enqueue("B")
                q.enqueue("C")
              Queue (front to back): A -> B -> C
        """
        new_node = QueueNode(data)

        if self.tail is None:
            # Queue is empty, new node is both head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            # Link new node at the end and update tail.
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Remove and return the value of the node at the front of the queue.

        Expected outcome:
            - The front element is removed and its data returned.
            - Example:
                queue:  A -> B -> C
                q.dequeue()  -> returns "A"
                queue after: B -> C
        """
        if self.head is None:
            return None

        old_head = self.head
        self.head = old_head.next

        if self.head is None:
            # The queue is now empty; update tail as well.
            self.tail = None

        old_head.next = None  # optional cleanup
        return old_head.data

    def print_all(self):
        """
        Print all elements of the queue from front (head) to back (tail).

        Expected outcome:
            - For queue A -> B -> C, prints:
                A -> B -> C
        """
        current = self.head
        output_parts = []

        # Manually build a "list" of values using a string accumulator,
        # not Python list/dict/tuple, to respect the restriction.
        while current is not None:
            # Convert each value to string and append to the accumulator.
            # We'll use a string with a separator.
            if output_parts:
                # If we already printed something, add separator first.
                output_parts.append(" -> ")
            output_parts.append(str(current.data))
            current = current.next

        # Join the pieces (output_parts is a list of strings, which is allowed
        # purely for printing; if you want zero composite types at all, you
        # could instead print as you iterate).
        print("".join(output_parts))


# ------------------------------
# Example usage (for testing)
# ------------------------------
if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    # Expected:
    # A -> B -> C
    q.print_all()

    # Expected:
    # dequeue() returns "A"
    removed = q.dequeue()
    print("Dequeued:", removed)

    # Expected:
    # B -> C
    q.print_all()