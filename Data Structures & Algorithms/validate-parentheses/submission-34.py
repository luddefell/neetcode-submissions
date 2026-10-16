class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ### Dictionary here with the open matching close
        pairs = {
            '[': ']',
            '{' : '}',
            '(' : ')'
        }
        if len(s)%2 == 1:
            return False
        for i in s:
            ## if this is an opened
            if i in pairs:
            ## add on to stack
                stack.append(i)
            ## else if its for a closed
            else:
                if not stack:
                    return False
                if (pairs[stack[-1]] != i) :
                    return False
                stack.pop()
        if stack:
            return False
        return True
            ### pop off the stack and compare if
            ##      if this not associated in the pairs with it then we are wrong and shouild be fasle
