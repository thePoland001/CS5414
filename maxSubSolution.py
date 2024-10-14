# Implementation of a max-subarray solution using cpp 

import math

def (MaxSubBruteForce, A, high, low): 
  left = low
  right = high 
  sum = -math.inf 
  for i in range (low, high):
    temp_sum = 0 
    for j in range (i, high): 
      temp_sum = temp_sum + A[j]
      if temp_sum > sum:
        sum = temp_sum 
        left = i
        right = j 
  return left, right, sum 

arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
ans = FindMaxSubarrayBruteForce(arr, 0, len(arr))

print(f"Max subarray = A[{ans[0] + 1}..{ans[1] + 1}] = {ans[2]}")

