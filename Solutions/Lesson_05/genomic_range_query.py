def solution(S, P, Q):
    result = [0] * len(P)

    for i in range(len(P)):
        sub_string = S[P[i]:Q[i]+1]

        if 'A' in sub_string:
            result[i] = 1
        elif 'C' in sub_string:
            result[i] = 2
        elif 'G' in sub_string:
            result[i] = 3
        else:
            result[i] = 4

    return result

