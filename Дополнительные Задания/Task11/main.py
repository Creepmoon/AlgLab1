from datetime import datetime
import os
import psutil


def Solution(size, length, array):
    dp = [[0] * (size + 1) for _ in range(length + 1)]
    for i in range(1, length + 1):
        for j in range(1, size + 1):
            dp[i][j] = dp[i - 1][j]
            if array[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - array[i - 1]] + array[i - 1])
    return dp[length][size]


process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt', 'r')
W, n = map(int, InputFile.readline().split())
array = list(map(int, InputFile.readline().split()))
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(W, n, array)))
OutputFile.close()
print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
