def prime(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for check in range(2, int(i ** 0.5) + 1):
            if i % check == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(*prime(10**6))