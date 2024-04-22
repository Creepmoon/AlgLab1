from datetime import datetime
import os
import psutil


def Solution(size, souvenirs):

    total_sum = sum(souvenirs)

    if total_sum % 3 != 0:
        return 0
    else:
        target_sum = total_sum // 3
        dp = [[0] * (target_sum + 1) for _ in range(size + 1)]

        for i in range(1, size + 1):
            for j in range(1, target_sum + 1):
                if souvenirs[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - souvenirs[i - 1]] + souvenirs[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        if dp[size][target_sum] == target_sum:
            return 1
        else:
            return 0

process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt', 'r')
n = int(InputFile.readline().strip())
array = list(map(int, InputFile.readline().strip().split()))
InputFile.close()

OutputFile = open('output.txt', 'w')
OutputFile.write(str(Solution(n,array)))
OutputFile.close()
OutputFile.close()
print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))