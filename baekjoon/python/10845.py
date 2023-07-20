# 상태 : 통과
# 어려웠던 점 : 포인터가 가르키고 있는게 정확히 어디인지 인지하면서 코딩하자.(rear에서 햇갈림)
import sys

input = sys.stdin.readline


class ImpleQueue:
    def __init__(self):
        self.data = []
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        self.data.insert(self.rear + 1, data)
        self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            result = self.data[self.front + 1]
            del self.data[self.front + 1]
            self.rear -= 1
            return result

    def size(self):
        return (self.rear + 1) - (self.front + 1)

    def isEmpty(self):
        if self.size() < 1:
            return 1
        else:
            return 0

    def front_data(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[self.front + 1]

    def back_data(self):
        if self.isEmpty():
            return -1
        else:
            return self.data[self.rear]


queue = ImpleQueue()

timese = int(input())
for i in range(timese):
    command = list(map(str, input().split()))
    if command[0] == "push":
        queue.enqueue(command[1])
    elif command[0] == "pop":
        print(queue.dequeue())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.isEmpty())
    elif command[0] == "front":
        print(queue.front_data())
    elif command[0] == "back":
        print(queue.back_data())
