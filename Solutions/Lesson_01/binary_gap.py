def solution(N):
    binary = '{0:0b}'.format(N)

    max_gap = 0
    current_gap = 0

    for b in binary:
        if b == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap = current_gap + 1

    return max_gap

