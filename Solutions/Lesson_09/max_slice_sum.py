def solution(A):
    slice_sum = 0
    max_sum = 0
    for _ in A:
        slice_sum += _
        max_sum = max(max_sum, slice_sum)
    return max_sum

