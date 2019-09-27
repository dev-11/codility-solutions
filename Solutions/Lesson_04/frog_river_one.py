def solution(X, A):
    B = [False] * max(A)
    counter = 0
    for _, elem in enumerate(A):
        idx = A[_] - 1
        if not B[idx]:
            B[idx] = True
            counter = counter + 1
        if counter == X:
            return _
    return -1

