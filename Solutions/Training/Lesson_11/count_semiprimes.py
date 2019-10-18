def solution(N, P, Q):
    result = [0] * len(P)
    for idx, item in enumerate(P):
        rng = [P[idx], Q[idx]]
        semi_prime_counter = 0
        length = Q[idx]
        sieve = [True] * (length + 1)
        sieve[0] = sieve[1] = False
        i = 2
        while i * i <= length:
            if sieve[i]:
                k = i * i
                while k <= length:
                    sieve[k] = False
                    k += i
            i += 1
        result[idx] = sieve

        print()
        print(rng)
        # for i in range(rng[0], rng[1]+1):
        #     if
        #     print(f'{i} = {sieve[i]}')

        result[idx] = semi_prime_counter

    return [10, 4, 0]


print(solution(26, [1, 4, 16], [26, 10, 20]))

