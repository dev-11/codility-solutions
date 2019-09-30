def solution(A):
    for _ in range(1, 100_000):
        if _ not in A:
            return _
    return -1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))

