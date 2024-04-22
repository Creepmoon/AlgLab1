from datetime import datetime
import os
import psutil

def Solution(height, Array):
    for i in range(len(Array)):
        Array[i][1] = Array[i][1] - Array[i][0]

        Array[i].append(i + 1)

    Array = sorted(Array, key=lambda Solution: Solution[1], reverse=True)

    Result = []
    while len(Array) > 0:
        for i in range(len(Array)):
            if height - Array[i][0] > 0:
                height += Array[i][1]
                Result.append(Array[i][2])
                del Array[i]
                break
            elif i == len(Array) - 1:
                return -1
    return str(Result).replace(",", "")[1:-1]

process = psutil.Process(os.getpid())
Start_time = datetime.now()

InputFile = open('input.txt', 'r')
Length, Height = map(int, InputFile.readline().split())

Array = []

for i in range(Length):
    Array.append(list(map(int, InputFile.readline().split())))

InputFile.close()


OutputFile = open('output.txt', 'w')
OutputFile.write((str((Solution(Height, Array)))))
OutputFile.close()

print(datetime.now() - Start_time, process.memory_info().rss / (1024 * 1024))
