#Reverse the order of the given string and return the string

str =" geeks quiz practice code"

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

s = Stack()
reverse_string = ""
for i in str:
    s.push(i)
    
while (s.is_empty() != True):
    reverse_string += s.pop()

print(str)
print(reverse_string)