class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        curr = self.head
        while curr and data > curr.data:
            prev = curr
            curr = curr.next

        new_node.next = curr
        prev.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
