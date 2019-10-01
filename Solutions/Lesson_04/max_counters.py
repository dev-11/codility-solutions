def solution(N, A):
    counters = [0] * N
    m = 0

    for i in range(len(A)):
        if A[i] <= N:
            counters[A[i] - 1] += 1
            m = max(m, counters[A[i] - 1])
        elif A[i] == N + 1:
            counters = [m] * N
    return counters

A = [0] * 7
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4
N = 5
print(solution(N, A))

