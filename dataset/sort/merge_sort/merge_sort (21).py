def sort_merge(sequence):
    if len(sequence) <= 1:
        return sequence

    middle = len(sequence) // 2
    first_part = sort_merge(sequence[:middle])
    second_part = sort_merge(sequence[middle:])

    return list(merge(first_part, second_part))

def merge(part1, part2):
    i, j = 0, 0
    while i < len(part1) and j < len(part2):
        if part1[i] <= part2[j]:
            yield part1[i]
            i += 1
        else:
            yield part2[j]
            j += 1

    yield from part1[i:]
    yield from part2[j:]