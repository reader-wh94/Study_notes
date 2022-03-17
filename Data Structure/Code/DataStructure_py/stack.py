class Stack:
    def __init__(self):
        self.stack = []
        
    def __len__(self):
        return len(self.stack)
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)
        else:
            print("Stack underflow")
            exit()
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack underflow")
            exit()
    
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty - True
        return is_empty

# test
s = Stack()
s.push(5)
print(s.peek())
s.push(4)
s.push(10)
s.push(7)
print(s.peek())
s.pop()
print(s.peek())