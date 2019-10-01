def solution(N, A):
    counters = [0] * N
    final_max = 0
    current_max = 0

    for item in A:
        if item <= N:
            if final_max > counters[item - 1]:
                counters[item - 1] = final_max
            counters[item - 1] += 1
            current_max = max(current_max, counters[item - 1])
        else:
            final_max = current_max

    counters = [max(final_max, item) for item in counters]

    return counters
