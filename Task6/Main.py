from datetime import datetime
import os
import psutil

def compare(Left, Right):
    Left = str(Left)
    Right = str(Right)

    for i in range(min(len(Left), len(Right))):
        if Left[i] < Right[i]:
            return True
        if Left[i] > Right[i]:
            return False

    if len(Left) < len(Right):
        return False
    if len(Left) > len(Right):
        return True
    return None

def Solution(array, length):
    if length <= 1:
        return array

    state_element = array[0]

    Higher = []
    Lower = []
    average = []

    for i in array:
        if compare(i, state_element) == False:
            Higher.append(i)
        elif compare(i, state_element) == True:
            Lower.append(i)
        else:
            average.append(i)

    Higher = Solution(Higher, len(Higher))
    Lower = Solution(Lower, len(Lower))

    return Higher + average + Lower


process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
Length = int(InputFile.readline())
Array = list(map(int, InputFile.readline().split()))
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(Array, Length)).replace(", ", "")[1:-1])
OutputFile.close()

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
