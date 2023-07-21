# 상태 : 불통
# 어려운 점: que로 재도전
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
numbers = list(range(1, n + 1))
target = k - 1
cycle = 0
print("<", end="")

"""
5번째가 아니라 4번째임
"""

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
        print(numbers[target], end=", ")
        del numbers[target]

        if target + k > len(numbers):
            target = (target + k) - len(numbers) - (cycle + 1)
            cycle += 1
        else:
            target += k - (cycle + 1)

print(">", end="")
