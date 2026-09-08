class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = data
        self.next = data


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtEnd(self, data):
        temp = Node(data)
        if(self.head is not None):
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.next = self.head
            temp.prev = t1
            self.head.prev = temp
        else:
            self.head = temp
            self.head.next = temp
            self.head.prev = temp
    
    def insertAtBeg(self, data):
        temp = Node(data)
        if(self.head is None):
            self.head = temp
            return
        temp.next = self.head
        temp.prev = self.head.prev
        self.head.prev.next = temp
        self.head.prev = temp
        self.head = temp
    
    def insertAtMid(self, data, x):
        temp = Node(data)
        t1 = self.head
        
        while(t1.next != self.head):
            if(t1.data == x):
                temp.next = t1.next
                t1.next.prev = temp
                temp.prev = t1
                t1.next = temp
                return
            t1 = t1.next
        temp.next = t1.next
        t1.next.prev = temp
        temp.prev = t1
        t1.next = temp

    def deleteLL(self, data):
        if(self.head is None):
            print("List is empty. Nothing to delete.")
            return

        temp = self.head
        
        if(temp.data == data):
            self.head = temp.next
            self.head.prev = temp.prev
            self.head.prev.next = self.head
            return
            
        temp = temp.next
        
        while(temp != self.head):
            if(temp.data == data):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next
            
        print(f"Error: Value '{data}' not found in the list.")
    
    def printLL(self):
        t1 = self.head
        if(t1 is None):
            print('LinkedList is Empty')
            return
        
        if(t1.next == self.head):
            print(t1.data, end=' ')
            return
        
        while(t1.next != self.head):
            print(t1.data, end=' ')
            t1 = t1.next
        print(t1.data, end=' ')
        

            
l1 = DoublyLinkedList()
l1.insertAtEnd(20)
l1.insertAtEnd(30)
l1.insertAtEnd(40)
l1.insertAtBeg(10)
l1.insertAtBeg(5)
l1.insertAtEnd(50)
l1.insertAtMid(500, 50)
l1.deleteLL(500)
l1.printLL()