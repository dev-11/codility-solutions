def solution(N, A):
    counters = [0] * N
    m = 0

    for item in A:
        if item <= N:
            counters[item - 1] += 1
            m = max(m, counters[item - 1])
        else:
            counters = [m] * N
    return counters
