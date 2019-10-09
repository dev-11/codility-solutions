def solution(K, A):
    rope_length = 0
    rope_count = 0
    
    for rope in A:
        rope_length += rope
        if rope_length >= K:
            rope_length = 0
            rope_count += 1

    return rope_count
    

print(solution(4, [1, 2, 3, 4, 1, 1, 3]))

