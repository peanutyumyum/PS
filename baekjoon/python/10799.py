# 상태 : 통과
# 어려웠던 점 : 이전에 작성한 코드는 뭔가 하나하나 다 카운트 하는 느낌으로 짰는데, 규칙을 찾는 식으로 머리를 쓰니깐 너무 쉽게 풀려버린 문제... 머리를 쓰자.

import sys

input = sys.stdin.readline

command = input()


class Queue:
    def __init__(self):
        self.data = []
        self.stick = 0

    def push(self, x):
        self.data.append(x)

    def isLazer(self):
        if self.data[-2] == "(":
            return True
        else:
            return False


queue = Queue()
result = 0

for i in command:
    if i == "(":
        queue.push(i)
        queue.stick += 1

    elif i == ")":
        queue.push(i)
        if queue.isLazer():
            queue.stick -= 1
            result += queue.stick
        else:
            queue.stick -= 1
            result += 1

print(result)
