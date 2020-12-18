import re
import fileinput

esum = 0
for line in fileinput.input('data/day18.txt'):
    tokens = line.rstrip().replace(' ', '')
    output = []
    operators = []
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '+' or token == '*':
            while operators and \
                    (operators[-1] != '(') and \
                    not (operators[-1] == '*' and token == '+'):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
    rpn = output+list(reversed(operators))
    stack = []
    for token in rpn:
        if token.isnumeric():
            stack.append(token)
        elif token == '*':
            result = int(stack.pop())*int(stack.pop())
            stack.append(result)
        elif token == '+':
            result = int(stack.pop())+int(stack.pop())
            stack.append(result)
        else:
            raise ValueError('unexpected thing in stack', token)
    print(stack[0])
    esum += stack[0]

print('total', esum)
