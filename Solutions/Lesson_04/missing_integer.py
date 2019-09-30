def solution(A):
    arr = sorted(set([item for item in A if item > 0]))

    n = len(arr) + 1
    total_sum = n * (n + 1) // 2

    return total_sum - sum(arr)

