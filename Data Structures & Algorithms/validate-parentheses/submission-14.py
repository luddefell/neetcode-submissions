class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        length = len(s)
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in pairs.keys():
                if len(stack) == 0 or stack[-1] != pairs[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False          
                    
                    

                
