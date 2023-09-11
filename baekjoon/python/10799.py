# 상태 : 불통

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
