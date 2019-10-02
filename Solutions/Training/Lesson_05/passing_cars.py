def solution(A):
    sum_of_pairs = 0
    pairs = 0
    for _ in A:
        if _ == 1:
            sum_of_pairs += pairs
        else:
            pairs += 1
        if sum_of_pairs > 1000000000:
            return -1
    return sum_of_pairs

