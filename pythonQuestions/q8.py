primes = [
    n
    for n in range(2, 101)
    if [
        d for d in range(2, int(n ** 0.5) + 1)
        if n % d == 0
    ] == []
]
print(primes)
