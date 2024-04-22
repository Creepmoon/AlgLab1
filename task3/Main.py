from datetime import datetime
import os
import psutil

def Solution(Length, CostArray, ClickArray):
    CostArray.sort()
    ClickArray.sort()
    result = 0
    for i in range(Length):
        result += CostArray[i] * ClickArray[i]

    return result
process = psutil.Process(os.getpid())
startTime = datetime.now()


InputFile = open('input.txt')
Length = int(InputFile.readline())
CostArray = list(map(int, InputFile.readline().split()))
ClickArray = list(map(int, InputFile.readline().split()))
InputFile.close()

result = Solution(Length, CostArray, ClickArray)
OutputFile = open('output.txt', 'w')
OutputFile.write(str(result))
OutputFile.close()

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
