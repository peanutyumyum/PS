# 

import sys
input = sys.stdin.readline

"(" "이면 push, " ")" "이면 pop"

times = int(input())

for i in range(times):
    parenthesis_string = input()

    stack = []
    size = 0
    for j in parenthesis_string:
        if j == "(":
            stack.append(j)
            size += 1
        elif j == ")":
            try:
                del stack[size - 1]
                size -= 1
            except IndexError as e:
                size = -1
                break

    
    if size != 0:
        print("NO")
    else:
        print("YES")