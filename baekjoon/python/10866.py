# 상태 : 통과
# 어려운 점  : 오타를 고치자^^

import sys

input = sys.stdin.readline


class DeQue:
    def __init__(self):
        self.data = []

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if self.isEmpty():
            return -1
        else:
            return self.data.pop(0)

    def pop_back(self):
        if self.isEmpty():
            return -1
        else:
            return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if self.size() > 0:
            return 0
        else:
            return 1

    def front(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[0]

    def back(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[-1]


times = int(input())
deque = DeQue()

for i in range(times):
    command = list(map(str, input().split()))
    if command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.isEmpty())
    elif command[0] == "front":
        print(deque.front())
    elif command[0] == "back":
        print(deque.back())
