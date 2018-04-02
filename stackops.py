class stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    
    def push(self,val):
        return self.stack.append(val)