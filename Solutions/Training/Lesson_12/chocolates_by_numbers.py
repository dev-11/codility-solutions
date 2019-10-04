def solution(N, M):
    empty_wrappers = []
    i = 0

    while i not in empty_wrappers:
        empty_wrappers.append(i)
        i = (i + M) % N

    return len(empty_wrappers)
