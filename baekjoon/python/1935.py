# 상태 : 불통
# 어려운 점 : 후위 표기법이 뭐야... 아니 친절하게 알려주면 얼마나 좋아;
# 다행히도 좋은 풀이법이 위의 사이트에 기재되어 있다. https://todaycode.tistory.com/73

import sys

input = sys.stdin.readline

N = int(input())
express = input()
number = [0] * N

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
