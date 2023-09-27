# 상태 : 통과
# 어려웠던 점 :
# 1. 이중 반복문을 사용할 경우 big(O)가 n^2 발생하므로 stack을 사용한다. (입력 값이 n < 1,000,000 이므로, big(0) = n 이어야 한다.)
# 2. n + n = 2n이다(n^2 아님)


"""
개선된 코드(big(o) ~= n)
크기를 검사하는 과정에서 현재 검사받는 숫자가 크다는 것은 이전 숫자에게도 큰 숫자일 수 있기 때문에 이를 착안하여 문제를 해결한다.

"""
import sys

input = sys.stdin.readline

times = int(input())
sequence = list(map(int, input().split()))
result = [-1] * times
stack = []

for i in range(times):
    while stack and sequence[i] > sequence[stack[-1]]:
        result[stack[-1]] = sequence[i]

        stack.pop()

    stack.append(i)
print(*result)


"""
원래 코드(big(O) = n^2)
근데 사실.. 이거도 worst가 n^2라 그렇지, nearly n인데.. 인덱싱이 시간이 많이 걸리나..
"""
import sys

input = sys.stdin.readline

times = int(input())

sequence = list(map(int, input().split()))


def find_num(n, index):
    for i in sequence[index:]:
        if n < i:
            return i

    return -1


for i in range(times):
    if i == times - 1:
        print(find_num(sequence[i], i), end="")
    else:
        print(find_num(sequence[i], i), end=" ")
