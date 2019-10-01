def solution(N, A):
    counters = [0] * N
    final_max = 0
    current_max = 0

    for item in A:
        if item <= N:
            counters[item - 1] = max(final_max, counters[item - 1]) + 1
            current_max = max(current_max, counters[item - 1])
        else:
            final_max = current_max

    counters = [max(final_max, item) for item in counters]

    return counters
