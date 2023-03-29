import sys

key = int(sys.argv[1])


def is_increasing(number: str) -> bool:
    for i in range(len(number) - 1):
        if number[i + 1] <= number[i]:
            return False

    return True


total = 0
for index in range(1, key):
    if is_increasing(str(index)):
        total += 1

print(total)
