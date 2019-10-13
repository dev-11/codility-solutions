def solution(A, B):
    if len(A) == 0:
        return 0

    counter = 1
    previous_end = B[0]
    for _ in range(1, len(A)):
        if A[_] > previous_end:
            counter += 1
            previous_end = B[_]

    return counter

