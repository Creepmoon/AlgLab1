from datetime import datetime

import os
import psutil

def Priorites(a, b, op):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '-':
        return a - b
    else:
        assert 0


def Solution(example):
    length = len(example)
    amountOfNumber = (length + 1) // 2

    minArray = [[0] * amountOfNumber for _ in range(amountOfNumber)]
    maxArray = [[0] * amountOfNumber for _ in range(amountOfNumber)]
    for i in range(amountOfNumber):
        minArray[i][i] = int(example[2 * i:2 * i + 1])
        maxArray[i][i] = int(example[2 * i:2 * i + 1])
    for s in range(amountOfNumber - 1):
        for i in range(amountOfNumber - s - 1):
            j = i + s + 1

            minVal, maxVal = float('inf'), float('-inf')


            for k in range(i, j):

                minmin = Priorites(minArray[i][k], minArray[k + 1][j], example[2 * k + 1])

                minmax = Priorites(minArray[i][k], maxArray[k + 1][j], example[2 * k + 1])

                maxmin = Priorites(maxArray[i][k], minArray[k + 1][j], example[2 * k + 1])

                maxmax = Priorites(maxArray[i][k], maxArray[k + 1][j], example[2 * k + 1])

                minVal, maxVal = min(minVal, minmin, minmax, maxmin, maxmax), max(maxVal, minmin, minmax, maxmin, maxmax)

            minArray[i][j] = minVal
            maxArray[i][j] = maxVal

    return maxArray[0][amountOfNumber - 1]


process = psutil.Process(os.getpid())
Start_time = datetime.now()

InputFile = open('input.txt', 'r')
example = InputFile.readline()
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(example)))

print(datetime.now() - Start_time, process.memory_info().rss / (1024 * 1024))