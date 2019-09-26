def solution(A):
    A.sort(reverse=True)
    for _ in range(len(A) - 2):
        if A[_] < A[_ + 1] + A[_ + 2]:
            return 1

    return 0

