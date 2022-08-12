import sys
input = sys.stdin.readline

S = int(input())

sigma_n = 0
number = 0

while True:
    sigma_n += number
    number += 1
    sigma_n_next = sigma_n + number
    if sigma_n <= S < sigma_n_next:
        break
print(number - 1)