def solution(A):
    arr = sorted(set([item for item in A if item > 0]))
    for index, item in enumerate(arr):
        if index + 1 != item:
            return index + 1
    return len(arr) + 1
