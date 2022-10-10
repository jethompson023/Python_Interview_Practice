"""
    Stack is a LIFO "Last In, First Out" algorithm
    With Stacks -> Insertion and deletion happen on the same end 
    Definitions for Stacks:
        1) Push(item) -> push item to the top of the stack 
        2) Pop(item) -> remove and return the top item
        3) Peek(item) -> return the top item without removing it
        4) Is_empty(item) -> return true if the stack is empty
"""

#Creatng a Class to represent a stack 
class Stack:
    def __init__(self): #constructor
        self.items = [] # items property of the class
    
    def is_empty(self):
        return len(self.items) == 0
        #OR
        #return not self.items     
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    s = Stack() #call the constructor
    print(s)
    print(s.is_empty())
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())