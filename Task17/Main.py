
from datetime import datetime
import os
import psutil


def Solution(length):
    Counts = [4, 2, 1, 0]
    bufferArray = [0 for _ in range(4)]

    if length > 1:
        for i in range(length - 1):
            bufferArray[0] += Counts[1] * 2 + Counts[2] * 2
            bufferArray[1] += Counts[0] + Counts[3] * 2
            bufferArray[2] += Counts[0]
            bufferArray[3] += Counts[1]
            Counts = bufferArray
            bufferArray = [0 for _ in range(4)]

        return sum(Counts) % 10**9
    else:
        return 8

process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
length_of_sequence = int(InputFile.readline())


OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(length_of_sequence)))

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))