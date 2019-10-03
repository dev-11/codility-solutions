def solution(N):
    i = 1
    min_perimeter = (i + N) * 2
    while i * i < N:
        if N % i == 0:
            min_perimeter = min(min_perimeter, (i + N//i) * 2)
        i += 1
    if i * i == N:
        min_perimeter = min(min_perimeter, (i + N // i) * 2)
    return min_perimeter
