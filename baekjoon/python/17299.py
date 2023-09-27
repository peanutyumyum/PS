# 상태 : 미정
# 해결 방법 :
# 1. n^2으로 보이는 문제를 n으로 만드려면, 정보를 어딘가에 저장하는 방식이어야 한다.
# 2. 수열안의 숫자들의 빈도를 나타낼 count라는 배열을 따로 만들어 사용한다. 해당 배열의 index는 수열에서의 숫자를 나타낸다.
# 3. count라는 배열과 원래 수열이 있다면, 이를 활용하여 오큰수(17298)을 구하는 문제와 다르지 않다.

import sys

input = sys.stdin.readline

times = int(input())
sequence = list(map(int, input().split()))

# 어떤 숫자들이 있는지 체크할 것임.
count = [0] * 1000001

stack = []
stack.append(0)

answer = [-1] * times

for i in sequence:
    count[i] += 1

for i in range(times):
    while stack and count[sequence[stack[-1]]] < count[sequence[i]]:
        answer[stack.pop()] = sequence[i]

    stack.append(i)

print(*answer)
