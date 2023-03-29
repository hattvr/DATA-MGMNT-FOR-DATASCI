import math
from typing import List, Tuple, Union

values = []
while True:
    line = int(input())
    if line == -12345:
        break
    values.append(line)


def check_conditionals(numbers: tuple) -> Union[None, Tuple[int, int, int]]:
    numbers = list(numbers)
    if not sum(numbers) == 0:
        return False  # Rule: Triple must equate to 0
    if len(numbers) != len(set(numbers)):
        return False  # Rule: Each value must be unique

    return True


def find_triples(numbers: list) -> List[Tuple[int, int, int]]:
    triples = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                triplet = (numbers[i], numbers[j], numbers[k])
                if check_conditionals(triplet):
                    triples.append(triplet)

    return triples


all_triples = find_triples(values)

if not all_triples:
    print("0 triples found")
    exit(1)

print(f"{len(all_triples)} triples found:")
for triple in all_triples:
    print(", ".join(map(str, triple)))
