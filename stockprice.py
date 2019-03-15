import math
def maxProfit(A, sday, eday):
    sday = int(sday)
    eday = int(eday)
    if sday == eday:
        return A[sday]
    else:
        midpoint = int(math.floor((sday + eday) / 2))
        #print(str(A[midpoint]))
        rightsum = 0
        counter = 0
        for i in range(int(midpoint+1), eday+1): #O(n/2)
            counter += A[i]
            if counter > rightsum:
                rightsum = counter
         
        counter = 0
        leftsum = 0
        for i in range(int(midpoint), sday-1, -1): #O(n/2)
            counter += A[i]
            if counter > leftsum:
                leftsum = counter
        
        #print(str(leftsum))
        #print(str(rightsum))
        sum = leftsum + rightsum
        return max(maxProfit(A, sday, midpoint), maxProfit(A, midpoint+1, eday), sum) #2T(n/2)
        # 2T(n/2) + n = O(nlogn)

A =  [-6, -1, +5, +7, +5, +3, -5, -7, -1, +10, +1, +5, -20, +10, +1]
print(str(maxProfit(A, 0, len(A)-1)))
print(str(maxProfit(A, 2, 11)))
A = [6, -50, 2, 13, 5, -14, 1, 6]
print(str(maxProfit(A, 0, len(A)-1)))