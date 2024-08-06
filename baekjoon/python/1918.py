# 상태 : 미정
# 어려웠던 점 :

import sys

input = sys.stdin.readline

express = input()

operand_stack = []
operator_stack = []
bracket = False
result = ""

for i in express:

    if operator_stack[-1] == "*" or operator_stack[-1] == "/" or i == ")":

        while operand_stack and operator_stack and 
    

    if i == "+" or i == "-" or i == "*" or i == "/":
        operator_stack.append(i)
    elif i == "(":
        bracket = True
    elif i == ")":
        bracket = False
    else:
        operand_stack.append(i)