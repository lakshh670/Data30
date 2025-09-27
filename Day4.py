
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [str(num) for num in range(1, 101) if is_prime(num)]
with open("primes.txt", "w") as f:
    f.write("\n".join(primes))

print("Prime numbers between 1 and 100 have been saved to 'primes.txt'")
