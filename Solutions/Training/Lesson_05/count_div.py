def solution(A, B, K):
    first = (A + K - 1) // K * K
    return 1 + (B - first) // K
