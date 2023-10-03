# 상태 : 통과
# 어려운 점 : 후위 표기법이 뭐야... 아니 친절하게 알려주면 얼마나 좋아;
# 다행히도 좋은 풀이법이 위의 사이트에 기재되어 있다. https://todaycode.tistory.com/73

# 위 사이트에 따르면, 후위표기식(postfix expression)은 피연산자가 먼저 나오고 그 다음에 연산자가 나오는 형태이다.
# 이 형태의 장점이라고 한다면 연산의 순서를 고려하지 않아도 된다는 것이다. 그냥 나열된 연산자의 순서대로 연산하면 된다.
# 이는 일반적으로 수학에서 사용하는 중위표기식이 연산의 우선순위가 있는 것(괄호나 곱셈 나눗셈에 우선순위를 부과한다.)과는 달리 나열된 순서대로 연산하면 된다는 장점이 있다.
# 때문에, 단순화 작업이 가능하여 컴퓨터가 연산할 때 사용하면 유익한 점이 있다.

# 추가적으로 딕셔너리를 이용하여, 알파벳에 해당하는 숫자를 색인해주자. (https://lazypazy.tistory.com/85)

import sys

input = sys.stdin.readline

N = int(input())
express = input()
number = [0] * N

stack = []

for i in range(N):
    number[i] = int(input())

for i in express:
    if i == "+" or i == "-" or i == "*" or i == "/":
        operand2 = stack.pop()
        operand1 = stack.pop()
        operator = i

        if operator == "+":
            value = operand1 + operand2
        elif operator == "-":
            value = operand1 - operand2
        elif operator == "*":
            value = operand1 * operand2
        else:
            value = operand1 / operand2

        stack.append(value)

    else:
        if i == "A":
            stack.append(number[0])
        elif i == "B":
            stack.append(number[1])
        elif i == "C":
            stack.append(number[2])
        elif i == "D":
            stack.append(number[3])
        elif i == "E":
            stack.append(number[4])
        elif i == "F":
            stack.append(number[5])
        elif i == "G":
            stack.append(number[6])
        elif i == "H":
            stack.append(number[7])
        elif i == "I":
            stack.append(number[8])
        elif i == "J":
            stack.append(number[9])
        elif i == "K":
            stack.append(number[10])
        elif i == "L":
            stack.append(number[11])
        elif i == "M":
            stack.append(number[12])
        elif i == "N":
            stack.append(number[13])
        elif i == "O":
            stack.append(number[14])
        elif i == "P":
            stack.append(number[15])
        elif i == "Q":
            stack.append(number[16])
        elif i == "R":
            stack.append(number[17])
        elif i == "S":
            stack.append(number[18])
        elif i == "T":
            stack.append(number[19])
        elif i == "U":
            stack.append(number[20])
        elif i == "V":
            stack.append(number[21])
        elif i == "W":
            stack.append(number[22])
        elif i == "X":
            stack.append(number[23])
        elif i == "Y":
            stack.append(number[24])
        elif i == "Z":
            stack.append(number[25])

result = stack.pop()
print(f"{result:.2f}")


"""
이전 풀이(후위표기식에 대해 잘못 이해하고 있었음.)

num_queue = []
operator_stack = []

for i in range(N):
    number[i] = int(input())

for i in express:
    while (
        num_queue
        and operator_stack
        and (i != "+" and i != "-" and i != "*" and i != "/")
    ):
        print(num_queue)
        print(operator_stack)
        operand1 = num_queue[0]
        operand2 = num_queue.pop(1)
        operator = operator_stack.pop(-1)
        print(operator)

        if operator == "+":
            value = operand1 + operand2
        elif operator == "-":
            value = operand1 - operand2
        elif operator == "*":
            value = operand1 * operand2
        else:
            value = operand1 / operand2

        num_queue[0] = value
        print(value)
        print(num_queue)

    if i == "+" or i == "-" or i == "*" or i == "/":
        operator_stack.append(i)
    else:
        if i == "A":
            num_queue.append(number[0])
        elif i == "B":
            num_queue.append(number[1])
        elif i == "C":
            num_queue.append(number[2])
        elif i == "D":
            num_queue.append(number[3])
        elif i == "E":
            num_queue.append(number[4])
        elif i == "F":
            num_queue.append(number[5])
        elif i == "G":
            num_queue.append(number[6])
        elif i == "H":
            num_queue.append(number[7])
        elif i == "I":
            num_queue.append(number[8])
        elif i == "J":
            num_queue.append(number[9])
        elif i == "K":
            num_queue.append(number[10])
        elif i == "L":
            num_queue.append(number[11])
        elif i == "M":
            num_queue.append(number[12])
        elif i == "N":
            num_queue.append(number[13])
        elif i == "O":
            num_queue.append(number[14])
        elif i == "P":
            num_queue.append(number[15])
        elif i == "Q":
            num_queue.append(number[16])
        elif i == "R":
            num_queue.append(number[17])
        elif i == "S":
            num_queue.append(number[18])
        elif i == "T":
            num_queue.append(number[19])
        elif i == "U":
            num_queue.append(number[20])
        elif i == "V":
            num_queue.append(number[21])
        elif i == "W":
            num_queue.append(number[22])
        elif i == "X":
            num_queue.append(number[23])
        elif i == "Y":
            num_queue.append(number[24])
        elif i == "Z":
            num_queue.append(number[25])

result = num_queue.pop()
print(result)
"""
