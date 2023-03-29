import math

values = []
while True:
    line = int(input())
    if line == -12345:
        break
    values.append(line)


def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 1:
        # Case One: An odd number of elements
        return numbers[len(numbers) // 2]
    else:
        # Case Two: An even number of elements
        m1 = numbers[len(numbers) // 2 - 1]
        m2 = numbers[len(numbers) // 2]

        return (m1 + m2) / 2


def standard_deviation(numbers: list) -> float:
    mean_value = mean(numbers)
    deviation = [(x - mean_value) ** 2 for x in numbers]
    variance = sum(deviation) / (len(numbers) - 1)
    return math.sqrt(variance)


output_str = (
    f"mean: {mean(values)}\n"
    f"median: {median(values)}\n"
    f"standard deviation: {standard_deviation(values)}"
)

print(output_str)
