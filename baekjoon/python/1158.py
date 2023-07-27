# 상태 : 통과
# 어려웠던 점 : %를 잘 이용하자.
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(range(1, N + 1))
target = K - 1
comma = ", "

print("<", end="")
for i in range(N):
    if len(numbers) == 1:
        comma = ""
    try:
        print(numbers[target], end=comma)
        del numbers[target]

        target = (target + K - 1) % len(numbers)
    except:
        pass

print(">", end="")

""" 
n, k = map(int, input().split())
numbers = list(range(1, n + 1))
target = k
cycle = 0
diff = 0
print("<", end="")

for i in range(n):
    if i == n - 1:
        print(numbers[target], end="")
        del numbers[target]

        if target + k > len(numbers):
            target = (target + k) - len(numbers) - (cycle + 1)
            cycle += 1
        else:
            target += k - (cycle + 1)
    else:
        print(numbers[target - 1], end=", ")
        if cycle != diff:
            

        if target + k <= len(numbers):
            target += k
        else:
            target = (target + k) - len(numbers)
            cycle += 1

print(">", end="") 
"""
