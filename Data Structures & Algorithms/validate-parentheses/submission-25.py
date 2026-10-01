class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = defaultdict(str)
        pairs = {
            '{' : '}',
            '(': ')',
            '[':']'
        }
        pairs['{'] = '}'
        pairs['('] = ')'
        pairs['[']= ']'
        if (len(s) %2) == 1:
            return False
        for i in s:
            if i in pairs:
                ## add to the stack
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if (pairs[stack[-1]] != i):
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        return True

                