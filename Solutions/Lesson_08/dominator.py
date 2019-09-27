def solution(A):
    if not len(A):
        return -1
    dict = {}
    for _ in A:
        if dict.get(_) == None:
            dict[_] = 1
        else:
            dict[_] += 1

    m = list(dict.keys())[list(dict.values()).index(max(dict.values()))]
    return A.index(m) if dict[m] > len(A) / 2 else -1

