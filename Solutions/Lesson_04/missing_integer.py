import numpy as np


def solution(A):
    arr = np.array(A)
    arr = set(arr[arr > 0])
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2

    return total_sum - sum(arr)


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))

