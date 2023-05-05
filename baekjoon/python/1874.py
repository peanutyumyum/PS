import sys

input = sys.stdin.readline

out = False
highest_push_num = 0

n = int(input())

result = ""
stack = []
size = 0

for i in range(n):
    out_num = int(input())

    if out:
        break

    # loop for push on the stack
    stack_condition = True
    while stack_condition:
        if size == 0:
            # first time
            if highest_push_num == 0:
                stack.append(1)
            # stack is empty, but it is not the first
            else:
                stack.append(highest_push_num + 1)
            size += 1
            result += "+\n"
        else:
            # pop from the stack
            if stack[-1] == out_num:
                # highest_push_num should be replaced
                if highest_push_num < stack[-1]:
                    highest_push_num = stack[-1]
                del stack[-1]
                size -= 1
                result += "-\n"
                stack_condition = False
            else:
                # this sequence is not work at this algorithm, so it need to stop for running
                if stack[-1] > out_num:
                    result = "NO"
                    stack_condition = False

                    out = True
                else:
                    # pushed number should be bigger than top number(toppest position number)
                    if highest_push_num > stack[-1]:
                        stack.append(highest_push_num + 1)
                    else:
                        stack.append(stack[-1] + 1)
                    size += 1
                    result += "+\n"

print(result)
