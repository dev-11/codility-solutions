def solution(A):
    count = []
    len_a = len(A)
    for i in range(len_a):
        sub_count = 0
        for j in range(len_a):
            if i != j and A[i] % A[j] != 0:
                sub_count += 1
        count.append(sub_count)
    return count


print(solution([3, 1, 2, 3, 6]))

