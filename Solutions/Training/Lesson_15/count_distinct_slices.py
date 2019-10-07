def solution(M, A):
    count = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            arr_slice = A[i:j+1]
            if len(arr_slice) == len(set(arr_slice)):
                print(f'({i}, {j}) = {arr_slice} == {set(arr_slice)}')
                count += 1
            else:
                j += 1

    return min(count, 1_000_000_000)
