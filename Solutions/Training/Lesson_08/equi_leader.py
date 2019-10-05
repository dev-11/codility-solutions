def solution(A):

    dictionary = {}

    for _ in A:
        if dictionary.get(_) is None:
            dictionary[_] = 1
        else:
            dictionary[_] += 1

    leader_count = max(dictionary.values())
    if leader_count <= len(A) / 2:
        return 0

    leader = list(
        dictionary.keys())[list(dictionary.values()).index(leader_count)]

    leader_on_right_count = leader_count
    leader_on_left_count = 0
    equi_leader = 0

    for i, item in enumerate(A):
        if item == leader:
            leader_on_left_count += 1
            leader_on_right_count -= 1

        if leader_on_left_count > (i+1) // 2 \
        and leader_on_right_count > (len(A)-i-1)//2:
            equi_leader += 1

    return equi_leader

