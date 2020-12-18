class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def printLL(self):
        if self.head:
            current = self.head
            while current is not None:
                print(f'{current.value} --> ', end='')
                current = current.next
        print("None")

    def __len__(self):
        count = 0
        if self.head:
            current = self.head
            while current is not None:
                count += 1
                current = current.next
        return count


ll = LinkedList()
ll.printLL()
ll.append(3)
ll.append(2)
ll.append(5)
ll.append(90)
ll.printLL()
print(len(ll))
