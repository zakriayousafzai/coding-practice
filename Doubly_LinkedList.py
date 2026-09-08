class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtEnd(self, data):
        temp = Node(data)
        if(self.head is not None):
            t1 = self.head
            while(t1.next is not None):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
        else:
            self.head = temp
    
    def insertAtBeg(self, data):
        temp = Node(data)
        if(self.head is None):
            self.head = temp
            return
        temp.next = self.head
        self.head = temp
    
    def insertAtMid(self, data, x):
        temp = Node(data)
        t1 = self.head
        
        while(t1 is not None):
            if(t1.data == x):
                temp.next = t1.next
                if(t1.next is not None):
                    t1.next.prev = temp
                temp.prev = t1
                t1.next = temp
                return
            t1 = t1.next
            
        print(f"Error: Target value '{x}' is not present in the LinkedList")

    def deleteLL(self, data):
        if(self.head is None):
            print("List is empty. Nothing to delete.")
            return

        temp = self.head
        
        if(temp.data == data):
            self.head = temp.next
            self.head.prev = None
            return
            
        temp = temp.next
        
        while(temp is not None):
            if(temp.data == data):
                temp.prev.next = temp.next
                if(temp.next is not None):
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            
        print(f"Error: Value '{data}' not found in the list.")
    
    def printLL(self):
        t1 = self.head
        if(t1 is None):
            print('LinkedList is Empty')
            return
            
        while(t1 is not None):
            print(t1.data, end=' ')
            t1 = t1.next

            
l1 = DoublyLinkedList()
l1.insertAtEnd(20)
l1.insertAtEnd(30)
l1.insertAtEnd(40)
l1.insertAtBeg(10)
l1.insertAtBeg(5)
l1.insertAtMid(500, 40)
l1.deleteLL(500)
l1.printLL()