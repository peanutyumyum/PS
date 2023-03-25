import sys
input = sys.stdin.readline

time = int(input())
for i in range(time):
    a, b = map(int, input().split())
    a_factorization = []
    b_factorization = []

    count = 2
    while count < 45000:
        if a % count == 0:
            a_factorization.append(count)
            a //= count
        if b % count == 0:
            b_factorization.append(count)
            b //= count
        if a % count != 0 and b % count != 0:
            count += 1
    
    common_multiple = []
    for a_number in a_factorization:
        for b_number in b_factorization:
            if a_number == b_number:
                common_multiple.append(a_number)
                a_factorization.remove(a_number)
                b_factorization.remove(b_number)
                break
    least_common_multiple_factorization = common_multiple
    least_common_multiple_factorization.extend(a_factorization)
    least_common_multiple_factorization.extend(b_factorization)
    print(least_common_multiple_factorization)
    least_common_multiple = 1
    for common_number in common_multiple:
        least_common_multiple *= common_number
    print(least_common_multiple)