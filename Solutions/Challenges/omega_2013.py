def solution(A, B):
    m = A[0]

    for i in range(len(A)):
        if A[i] < m:
            m = A[i]
        if A[i] > m:
            A[i] = m

    j = len(A) - 1
    count = 0

    while j >= 0 and count < len(B):
        if A[j] >= B[count]:
            count += 1

        j -= 1

    return count
