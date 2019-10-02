def solution(A):
    if not len(A):
        return -1
    dictionary = {}
    for _ in A:
        if dictionary.get(_) is None:
            dictionary[_] = 1
        else:
            dictionary[_] += 1

    m = list(dictionary.keys())[list(dictionary.values()).index(max(dictionary.values()))]
    return A.index(m) if dictionary[m] > len(A) / 2 else -1

