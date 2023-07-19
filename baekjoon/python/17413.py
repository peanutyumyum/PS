# 상태 : 통과
# 어려웠던 점 : 함수의 before assignment 문제를 global을 통해 해결할 것.
import sys

input = sys.stdin.readline
word_line = input()
stack = []
lock = False


def suffle_and_print():
    global stack
    stack.reverse()
    if stack != []:
        for j in stack:
            print(j, end="")
    print(" ", end="")
    stack = []


def suffle_and_print_last():
    global stack
    stack.reverse()
    if stack != []:
        for j in stack:
            print(j, end="")


for i in word_line:
    if i == "<" or lock:
        lock = True
        if i == ">":
            lock = False
        if stack != []:
            stack.reverse()
            for j in stack:
                print(j, end="")
            stack = []
        print(i, end="")

    else:
        if i == " ":
            suffle_and_print()
        elif word_line[-1] == i:
            suffle_and_print_last()
        elif i != " ":
            stack.append(i)
