
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        if self.head is None:
            print("Empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")


# Testing
ll = CLL()

ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()
