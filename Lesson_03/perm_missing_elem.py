def solution(A):
    n = len(A)
    correct_sum = (n+1)*(n+2)//2
  
    for i in range(n):
       correct_sum = correct_sum - A[i]

    return correct_sum

