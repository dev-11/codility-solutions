def solution(X, A):
    B = [False] * max(A)
    counter = 0
    for index, _ in enumerate(A):
        idx = A[index] - 1
        if not B[idx]:
            B[idx] = True
            counter = counter + 1
        if counter == X:
            return index
    return -1

