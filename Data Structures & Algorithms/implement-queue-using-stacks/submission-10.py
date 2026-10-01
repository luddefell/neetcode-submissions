class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) > 0: 
            self.stack1.append(x)
        elif len(self.stack2) > 0:
            self.stack2.append(x)
        else:
            self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack1:
            while len(self.stack1) != 1:
                self.stack2.append(self.stack1.pop())
            return_val = self.stack1.pop()
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
            return return_val
        elif self.stack2:
            while len(self.stack2) != 1:
                self.stack1.append(self.stack2.pop())
            return_val = self.stack2.pop()
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return return_val
        else:
            return
        
        

    def peek(self) -> int:
        if self.stack1:
            print(self.stack1)
            while len(self.stack1) != 1:
                self.stack2.append(self.stack1.pop())
            last_one = self.stack1.pop() 
            self.stack2.append(last_one)
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
            print(self.stack2)
            return last_one
        elif self.stack2:
            while len(self.stack2) != 1:
                self.stack1.append(self.stack2.pop())
            last_one = self.stack2.pop() 
            self.stack1.append(last_one)
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return last_one
        else:
            return
        
        

    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()