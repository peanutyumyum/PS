import sys
input = sys.stdin.readline

string = input()
cursor = -1
input_time = int(input())

for i in range(input_time):
    command = input()
    if command[0] == "L":
        # if cursor not placed in left
        if cursor > -(len(string) + 1):
            cursor -= 1
    elif command[0] == "D":
        if cursor < -1:
            cursor += 1
    elif command[0] == "B":
        if cursor > -(len(string) + 1) and len(string) != 0:
            del string[cursor]
    elif command[0] == "P":
        string = string[:cursor] + command[-2] + string[cursor:]
        print(string[:cursor], string[cursor:], command[-2])

print(string)
