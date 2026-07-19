# Memory: 8.2 MB•Time: 45ms•Submitted at: 07/19/2026 10:59

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        
        for _ in range(k):
            node = Node(None)

            # Initialize first node, or increment tail
            if self.head is None:
                self.head = node
            else:
                # Connect previous node
                self.tail.next = node

            self.tail = node

        # Create circular connection
        self.tail.next = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = self.tail.next
        self.tail.data = value
        return True        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head.data = None
        self.head = self.head.next
        return True

    def Front(self) -> int:
        if self.head.data is not None:
            return self.head.data  
        else: 
            return -1
        

    def Rear(self) -> int:
        if self.tail.data is not None:
            return self.tail.data
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.head.data is None:
            return True 
        else:
            return False
        
    def isFull(self) -> bool:
        if self.head.data is not None and self.tail.next == self.head:
            return True  
        else:
            return False
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
