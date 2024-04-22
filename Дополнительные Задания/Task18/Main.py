from datetime import datetime
import os
import psutil


def Solution(couponsCount, price):
    A = [[100000 for _ in range(couponsCount + 1)] for _ in range(couponsCount + 1)]
    A[0][0] = 0
    coupons = [0, 0]
    lunch = []
    for i in range(1, len(A)):
        for j in range(len(A[0]) - 1):
            if price[i - 1] <= 100:
                A[i][j] = min(A[i - 1][j] + price[i - 1], A[i - 1][j + 1])
            else:
                A[i][j] = min(A[i - 1][j - 1] + price[i - 1], A[i - 1][j + 1])
    minimum = min(A[couponsCount])
    for i in range(couponsCount):
        if minimum == A[couponsCount][i]:
            coupons[0] = i
    j = coupons[0]
    i = couponsCount
    coupons[1] = 0
    while i != 0 or j != 0:
        if price[i - 1] <= 100:
            if A[i - 1][j] + price[i - 1] <= A[i - 1][j + 1]:
                i -= 1
            else:
                lunch.append(i)
                i -= 1
                j += 1
                coupons[1] += 1
        else:
            if A[i - 1][j - 1] + price[i - 1] <= A[i - 1][j + 1]:
                i -= 1
                j -= 1
            else:
                lunch.append(i)
                i -= 1
                j += 1
                coupons[1] += 1
    return minimum, coupons, sorted(lunch)


process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt', 'r')
days = int(InputFile.readline())
price = []
for i in range(days):
    price.append(int(InputFile.readline()))

OutputFile = open('output.txt', 'w')
if 1 <= days <= 10 ** 2 and min(price) >= 0 and max(price) < 300:
    answer, coupons, coupon_days = Solution(days, price)
    OutputFile.write(str(answer) + '\n')
    for coupon in coupons:
        OutputFile.write(str(coupon) + ' ')
    for day in coupon_days:
        OutputFile.write('\n' + str(day))

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
