class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SSL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        
        while current.next is not None:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head

        while current:
            print(current.data,end="->")
            current = current.next

    def delete_last(self):
        if self.head is None:
            print("\nList is empty")
            return

        if self.head.next is None:
            self.head = None
            print("\nLast node deleted successfully!")
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None
        print("\nLast node deleted successfully!")


s = SSL()
s.insert(10)
s.insert(20)
s.insert(20)
s.display()
s.delete_last()
s.display()

