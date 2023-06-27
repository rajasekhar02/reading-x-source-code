import math
# Learnings: Modulo Arthimetic
# Addition: ( a + b) % c = ( ( a % c ) + ( b % c ) ) % c
# Multiplication: ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c
# Subtraction: ( a – b) % c = ( ( a % c ) – ( b % c ) ) % c
# Division: find gcd(b, m), if gcd(b,m) > -1: ((b^m-2)%m * a)%m
def evaluatePostfix(exp):
    # Write your code here.
    strs = exp
    stack = []
    constant = int((1e9)+7)
    for i in strs:
        if i == "*":
            operand1 = stack.pop()
            operand2 = stack.pop()
            val = (operand2 % constant)*(operand1 % constant)
            val = val % constant
            stack.append(val)
        elif i == "+":
            operand1 = stack.pop()
            operand2 = stack.pop()
            val = (operand2 % constant)+(operand1 % constant)
            val = val % constant
            stack.append(val)
        elif i == "-":
            operand1 = stack.pop()
            operand2 = stack.pop()
            val = (operand2 % constant) - (operand1 % constant) + constant
            val = val % constant
            stack.append(val)
        elif i == "/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            g = math.gcd(operand1, constant)
            val = 1
            if g > -1:
                inv = pow(operand1, constant-2, constant)
                val = inv*operand2
            # val = operand2 / operand1
                val = val % constant
            stack.append(val)
        else:
            stack.append(int(i))
    return stack[-1]
