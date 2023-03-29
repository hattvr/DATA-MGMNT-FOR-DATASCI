import sys

key = int(sys.argv[1])


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


prime_values = []
for i in range(2, key):
    if is_prime(i):
        prime_values.append(i)

print(" ".join(map(str, prime_values)))
