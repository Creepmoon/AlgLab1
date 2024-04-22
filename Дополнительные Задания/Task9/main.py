from cmath import inf
from datetime import datetime
import os
import psutil

def Solution(array, count):
    array.sort(key=lambda amount: amount[2])
    min_in, min_sum = inf, 0
    N_ = count
    for i in array:
        if i[0] > count and i[1] < min_in:
            min_in = i[1]
            continue
        while N_ >= i[0]:
            N_ -= i[0]
            min_sum += i[1]
    return min(min_in, min_sum)

process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
N = int(InputFile.readline())
numbers = [[10 ** j, int(InputFile.readline())] for j in range(7)]
numbers = list(map(lambda k: [k[0], k[1], k[1] / k[0]], numbers))
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(numbers, N)))

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))