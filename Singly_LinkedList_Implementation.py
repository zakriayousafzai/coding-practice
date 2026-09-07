class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtEnd(self, data):
        temp = Node(data)
        if(self.head is not None):
            t1 = self.head
            while(t1.next is not None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBeg(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    def insertAtMid(self, data, x):
        temp = Node(data)
        t1 = self.head
        
        while(t1 is not None):
            if(t1.data == x):
                temp.next = t1.next
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
            return
            
        prev = temp
        temp = temp.next
        
        while(temp is not None):
            if(temp.data == data):
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            
        print(f"Error: Value '{data}' not found in the list.")
    
    def printLL(self):
        t1 = self.head
        if(t1 is None):
            print('LinkedList is Empty')
            return
            
        while(t1 is not None):
            print(t1.data)
            t1 = t1.next

            
l1 = LinkedList()
l1.insertAtEnd(20)
l1.insertAtEnd(40)
l1.insertAtBeg(10)
l1.insertAtMid(30, 20)
l1.insertAtMid(50, 40)
l1.printLL()