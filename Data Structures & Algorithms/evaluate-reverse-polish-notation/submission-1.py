class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(a,b,i):
            if i == '+':
                return a+b
            elif i == "-":
                return a-b
            elif i == '/':
                return a/b
            else:
                return a*b

        stack= []
        for i in tokens:
            if i not in '+-/*':
                stack.append(int(i))
            else:
                b,a = stack.pop(),stack.pop()
                stack.append(eval(a,b,i))
        return stack[0]
