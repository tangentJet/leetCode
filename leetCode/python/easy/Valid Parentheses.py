class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"(":")", "{":"}","[":"]"}
        stack = []
        for c in s:
            if c in pars.keys():
                stack.append(pars.get(c))
            elif len(stack) == 0:
                return False
            elif c == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            print(3, stack)
            return False