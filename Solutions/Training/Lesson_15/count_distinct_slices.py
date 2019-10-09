def solution(M, A):
    total_count = 0
    sub_count = 0
    front = 0
    len_a = len(A)
    uniques = set()

    for back in range(len_a):
        while front < len_a and A[front] not in uniques:
            uniques.add(A[front])
            front += 1
            sub_count += 1

        uniques.remove(A[back])

        back += 1
        total_count += sub_count
        sub_count -= 1

    return min(total_count, 1000000000)
