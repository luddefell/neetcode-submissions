class MyQueue:

    def __init__(self):
        self._stack = []
        

    def push(self, x: int) -> None:
        self._stack.append(x)
        
        

    def pop(self) -> int:
        new_stack = []
        return_val = self._stack[0]
        for i in self._stack[1:]:
            new_stack.append(i)
        self._stack = new_stack
        return return_val

    def peek(self) -> int:
        return self._stack[0]

    def empty(self) -> bool:
        return (len(self._stack) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()