def solution(A):
    index = 0
    min_avg = (A[0] + A[1]) / 2

    for idx in range(2, len(A)):
        avg_1 = (A[idx - 1] + A[idx]) / 2
        avg_2 = (A[idx - 2] + A[idx - 1] + A[idx]) / 3
        if avg_1 < min_avg:
            index = idx - 1
            min_avg = avg_1
        if avg_2 < min_avg:
            index = idx - 2
            min_avg = avg_2

    return index

