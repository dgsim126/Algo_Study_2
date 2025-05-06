# def solution(number):
#     prime = {}
#     while True:
#         is_seperate = False
#         if number == 1:
#             break
#         for i in range(2, int(number**(1/2) + 1)):
#             if number % i == 0:
#                 if i in prime:
#                     prime[i] += 1
#                     number = number // i
#                     is_seperate = True
#                     break
#                 else:
#                     prime[i] = 1
#                     number = number // i
#                     is_seperate = True
#                     break
#         if not is_seperate:
#             last = False
#             for i in range(2, number+1):
#                 if number % i == 0:
#                     last = True
#                     if i in prime:
#                         prime[i] += 1
#                         number = number // i
#                     else:
#                         prime[i] = 1
#                         number = number // i
#             if not last:
#                 break
#             else:
#                 continue
    
#     print(prime)

# solution(987654321)


def solution(number):
    prime = {}
    i = 2
    while i * i <= number:
        while number % i == 0:
            prime[i] = prime.get(i, 0) + 1
            number //= i
        i += 1
    if number > 1:
        prime[number] = prime.get(number, 0) + 1

    return prime

def format_prime_factors(prime_factors: dict) -> str:
    items = sorted(prime_factors.items())
    parts = [
        f"{factor}^{count}" if count > 1 else f"{factor}"
        for factor, count in items
    ]
    return " * ".join(parts)

factors = solution(987654321)
formatted = format_prime_factors(factors)
print(formatted)