numbers = [2, 3]
for i in range(5, 1000000):
    is_prime = True
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        numbers.append(i)

print(*numbers)