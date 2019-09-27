def solution(A):
    left = sum(A[1:])
    right = A[0]
    m = abs(left - right)
    for _ in range(1, len(A) - 1):
        left -= A[_]
        right += A[_]
        m = min(abs(left - right), m)

    return m

