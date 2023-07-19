# 단어 뒤집기
# 어려웠던 점  : big O가 n3이라..

import sys
input = sys.stdin.readline

times = map(str, input().split("<"))

for i in range(times):
    words_list = list(map(str, input().split()))
    for j in words_list:
        word = j
        stack = []
        size = 0
        for k in word:
            stack.append(k)
            size += 1
        
        reverse_time = size
        for l in range(reverse_time):

            print(stack[size - 1], end="")
            del stack[size - 1]
            size -= 1
        print(" ", end="")

    print()
