def solution(A):
    slice_sum = A[0]
    max_sum = A[0]
    for _ in range(1, len(A)):
        slice_sum = max(A[_], slice_sum + A[_])
        max_sum = max(max_sum, slice_sum)
    return max_sum

