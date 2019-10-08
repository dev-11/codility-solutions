def solution(A):
    A.sort()
    n = len(A)
    result = 0
    for x in range(n):
        z = x + 2
        for y in range(x + 1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result

