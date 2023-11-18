class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insertAtPos(self, data, index):
        if index == 0:
            self.insertAtBeg(data)
        else:
            node = Node(data)
            curr = self.head
            
            while index > 1 and curr is not None:
                curr = curr.next
                index -= 1
            node.next = curr.next
            curr.next = node

ll = LinkedList()
ll.insertAtBeg(4)
ll.insertAtBeg(3)
ll.insertAtBeg(2)
ll.insertAtBeg(1)
ll.insertAtPos(5,0)

while ll.head is not None:
    print(ll.head.data)
    ll.head = ll.head.next
