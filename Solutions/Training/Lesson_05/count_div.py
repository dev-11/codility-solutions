def solution(A, B, K):
    first = (A + K - 1) // K * K
    return 1 + (B - first) // K

print(solution(6, 11, 2))
print(solution(0, 0, 11))

