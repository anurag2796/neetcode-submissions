class Solution:
    def isValid(self, s: str) -> bool:
        
        stk= []
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if i == '{' or i == '[' or i == '(':
                    stk.append(i)
                else:
                    if (i == ']' and stk[-1] == '[') or (i == '}' and stk[-1] == '{') or (i == ')' and stk[-1] == '('):
                        stk.pop()
                    else:
                        return False

        if not stk:
            return True
        return False                    