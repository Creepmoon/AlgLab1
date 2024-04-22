from datetime import datetime
import os
import psutil

def Solution(items, size):
    items.sort(key = lambda item: (item[0] / item[1]), reverse=True)
    taken = 0
    max_parts = 0
    for k, current in items:
        if taken + current <= size:
            max_parts += k
            taken += current
        else:
            max_parts += (k / current) * (size - taken)
            break
    return round(max_parts, 4)

process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
count, size = list(map(int, InputFile.readline().split()))
array = [list(map(int, InputFile.readline().split())) for i in range(count)]
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(array,size)))
OutputFile.close()
print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))



