def solution(A):

    unique_number = 0

    for _ in A:
        unique_number ^= _

    return unique_number

