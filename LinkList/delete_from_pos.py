
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

    def delete_pos(self, pos):
        if self.head is None:
            print("\nList is empty")
            return

        if pos < 0:
            print("\nInvalid position")
            return

        if pos == 0:
            self.head = self.head.next
            print("\nNode deleted successfully!")
            return

        current = self.head
        count = 0

        while current.next is not None and count < pos - 1:
            current = current.next
            count += 1

        if current.next is None:
            print("\nPosition not found")
            return

        current.next = current.next.next
        print("\nNode deleted successfully!")
s = SSL()
s.insert(10)
s.insert(20)
s.insert(20)
s.display()
s.delete_pos(2)
s.display()
