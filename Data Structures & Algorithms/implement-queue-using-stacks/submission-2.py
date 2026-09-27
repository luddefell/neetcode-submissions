class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        

    def push(self, x: int) -> None:
        self._stack1.append(x)
        
        

    def pop(self) -> int:
        while self._stack1:
            if len(self._stack1) == 1:
                result = self._stack1.pop()
            else: 
                self._stack2.append(self._stack1.pop())
        while self._stack2:
            self._stack1.append(self._stack2.pop())
        return result



    def peek(self) -> int:
        while self._stack1:
            if len(self._stack1) == 1:
                result = self._stack1[-1]
            self._stack2.append(self._stack1.pop())
        while self._stack2:
            self._stack1.append(self._stack2.pop())
        return result

    def empty(self) -> bool:
        return (len(self._stack1) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()