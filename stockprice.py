import math
def maxProfit(A, sday, eday):
    if sday == eday:
        return A[sday]
    else:
        midpoint = math.floor((sday + eday) / 2)
        sum = 0
        for i in range(sday, eday + 1): #O(n)
            sum += A[i]
        return max(maxProfit(A, sday, midpoint), maxProfit(A, midpoint+1, eday), sum) #2T(n/2)
        # 2T(n/2) + n = O(nlogn)

A =  [6, -50, 2, 13, 5, -14, 1, 6]
print(str(maxProfit(A, 0, 7)))