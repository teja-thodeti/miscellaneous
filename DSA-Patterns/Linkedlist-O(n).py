# Node class represents each guest at the party
class Node:
    def __init__(self, data):
        self.data = data    # Store the actual value (the gift)
        self.next = None    # Pointer to the next node (next guest). Starts as None.

# LinkedList class manages the entire party
class LinkedList:
    def __init__(self):
        self.head = None    # The first guest in the party (start of the list)

    def insert_at_end(self, data):
        # Step 1: Create a new node with the data
        new_node = Node(data)

        # Step 2: If the party is empty (head is None), new node becomes the head
        if self.head is None:
            self.head = new_node
            return  # We're done here

        # Step 3: Otherwise, start from the head and find the last node
        temp = self.head
        while temp.next:  # While there's a next node, keep moving forward
            temp = temp.next

        # Step 4: Link the last node's next to the new node (adding the new guest at the end)
        temp.next = new_node

    def delete_value(self, data):
        # Step 1: Start from the head
        temp = self.head
        prev = None  # We need to remember the previous node

        # Step 2: If head itself holds the data to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next  # Move head to the next node, dropping the current head
                temp = None  # Help garbage collection
                return

        # Step 3: Search for the node to delete, keep track of previous node
        while temp is not None:
            if temp.data == data:
                break  # Found the node to delete
            prev = temp
            temp = temp.next

        # Step 4: If data was not found in the list
        if temp is None:
            print(f"Value {data} not found in the list.")
            return

        # Step 5: Unlink the node from the linked list
        prev.next = temp.next
        temp = None  # Help garbage collection

    def display(self):
        # Step 1: Start from head
        temp = self.head

        # Step 2: Traverse the list and print all node data
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")  # End of list

# ====== TEST THE WHOLE THING ======
ll = LinkedList()

ll.insert_at_end(10)   # Insert 10, list: 10 -> None
ll.insert_at_end(20)   # Insert 20, list: 10 -> 20 -> None
ll.insert_at_end(30)   # Insert 30, list: 10 -> 20 -> 30 -> None

ll.display()           # Output: 10 -> 20 -> 30 -> None

ll.delete_value(20)    # Delete node with value 20, list: 10 -> 30 -> None

ll.display()           # Output: 10 -> 30 -> None

ll.delete_value(40)    # Try to delete non-existent value 40, prints warning
