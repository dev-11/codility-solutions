def solution(A):
    n = len(A)+1
    total_sum = n * (n + 1)//2

    return total_sum - sum(A)

