from datetime import datetime
import os
import psutil


def Solution(array):
    stack = []
    result = ''
    openStr = {'(', '[', '{'}
    closeStr = {')': '(', ']': '[', '}': '{'}
    to_remove = []

    for i, char in enumerate(array):
        if char in openStr:
            stack.append((char, i))
        elif char in closeStr:
            if not stack or stack[-1][0] != closeStr[char]:
                to_remove.append(i)
            else:
                stack.pop()

    for bracket, i in stack:
        to_remove.append(i)

    for i, char in enumerate(array):
        if i not in to_remove:
            result += char

    return result


process = psutil.Process(os.getpid())
startTime = datetime.now()
InputFile = open('input.txt', 'r')
array = InputFile.readline().strip()
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(Solution(array))
OutputFile.close()

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
