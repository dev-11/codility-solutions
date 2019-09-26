def solution(A):
    sum = 0
    pairs = 0
    for _ in A:
        if _ == 1:
            sum += pairs
        else:
            pairs += 1
        if sum > 1000000000:
            return -1
    return sum


print(solution([0, 1, 0, 1, 1]))

