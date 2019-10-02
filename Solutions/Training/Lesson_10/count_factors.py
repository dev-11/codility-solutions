def solution(N):
    factorCount = 0;

    for i in range(1, N):
        if N%i == 0:
            factorCount += 1

    return factorCount

print(solution(24))
