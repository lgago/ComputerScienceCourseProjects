'''main.py Luis Gago CS2420, no help from other students'''
from stack import Stack

def equal_or_higher(top, next_input):
    '''returns true is the precidence of the top is greater or equal to the next_input'''
    if top in ('*', "/"):
        return True
    if next_input in ("*", "/"):
        return False
    return True

def in2post(expr):
    '''converts infix to postfix expression'''
    if not isinstance(expr, str):
            raise ValueError('error, expression must be a string')
    expr = expr.replace(" ", "")
    postfix = ""
    stack = Stack()
    for values in expr:
        if values == "(":
            stack.push(values)
        elif values.isdigit():
            postfix += values
        elif values == '+' or values == "-" or values == "*" or values == "/":
            while stack.size() > 0 and stack.peek() != "(" and equal_or_higher(stack.peek(), values):
                #print(stack.peek())
                postfix += stack.pop()
            stack.push(values)
        else:
            #print(stack.peek())
            postfix += stack.pop()
            if stack.size() == 0:
                raise SyntaxError("Inalid Expression.")
            while stack.peek() != "(":
                #print(stack.peek())
                postfix += stack.pop()
            stack.pop()
    while stack.size() > 0:
        #print(stack.peek())
        postfix += stack.pop()
    return postfix

def eval_postfix(expr):
    '''evaluate the postfix'''
    if not isinstance(expr, str):
            raise ValueError('error, expression must be a string')
    expr = expr.replace(" ", "")
    stack = Stack()
    for values in expr:
        if values.isdigit():
            stack.push(values)
        else:
            if stack.size() < 2:
                raise SyntaxError("Inalid Expression.")
            first_num = stack.pop()
            second_num = stack.pop()
            push_num = str(second_num) + str(values) + str(first_num)
            push_num = eval(push_num)
            stack.push(push_num)
    if stack.size() > 1:
        raise SyntaxError("Inalid Expression.")
    return float(stack.pop())

def main():
    '''main function'''
    file_import = open("data.txt", "r")
    for item in file_import:

        print("infix:", item.strip())
        print("postfix:", in2post(item.strip()))
        print("answer:", eval_postfix(in2post(item.strip())), "\n")

if __name__ == "__main__":
    main()
