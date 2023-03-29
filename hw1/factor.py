import sys

key = int(sys.argv[1])


def find_factors(number: int) -> list:
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


print(" ".join(map(str, find_factors(key))))
