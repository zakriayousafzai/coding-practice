class Stack:
    def __init__(self):
        self.stack = []
    
    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.stack.pop()
    
    def length(self):
        return len(self.stack)
    

obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.pop()
print("Length:", obj.length(),"\nLast Element:", obj.peek())