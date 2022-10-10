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

string = "gninraeL nIdekniL htiw a nraeL"
reverse_string = ""

s = Stack()

#Your Answer
for i in string: 
    s.push(i)

while (s.is_empty() != True):
    reverse_string += s.pop()


# for char in string:
#     s.push(char)

# while not s.is_empty():
#     reverse_string += s.pop()

print(reverse_string)