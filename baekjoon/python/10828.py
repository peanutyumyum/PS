# Implemet Stack
# 어려웠던 점  : 몸체를 만드는 것보단, 오랜만에 파이썬을 쓰다보니.. list사용할 땐 완전 빈 공간과 0으로 초기화 되어 있는 부분을 잘 구분해야겠다!

import sys
input = sys.stdin.readline


class Stack():

    def __init__(self):
        self.data = []
        self.sizes = 0
    
    def push(self, x):
        self.data.append(int(x))
        self.sizes += 1
    
    def pop(self):
        if self.empty():
            return -1
        else:
            self.sizes -= 1
            output = self.data[self.sizes]
            del self.data[self.sizes]
            return output
    
    def size(self):
        return self.sizes

    def empty(self):
        if self.sizes == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[self.sizes - 1]

stack = Stack()

time = int(input())

for i in range(time):
    
    command = list(map(str, input().split()))
    if command[0] == "push":
        stack.push(command[1])
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())