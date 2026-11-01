class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operator = {"*", "+", "-", "/"}
        stk=[]
        result =0
        for i in range (0, len(tokens)):
            if tokens[i] in operator:
                b = stk.pop()
                a = stk.pop()
                if tokens[i] == '+':
                    result = a + b
                elif tokens[i] == '-':
                    result = a - b
                elif tokens[i] == '*':
                    result = a * b
                elif tokens[i] == '/':
                    result = int(a / b)
                stk.append(result)
            else:
                stk.append(int(tokens[i]))
        return stk.pop()
