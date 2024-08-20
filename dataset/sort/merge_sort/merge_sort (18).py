def sort_merge(sequence):
    if len(sequence) <= 1:
        return sequence

    middle = len(sequence) // 2
    first_half = sequence[:middle]
    second_half = sequence[middle:]

    first_half = sort_merge(first_half)
    second_half = sort_merge(second_half)

    return combine(first_half, second_half)

def combine(part1, part2):
    combined = []
    i, j = 0, 0

    while i < len(part1) and j < len(part2):
        if part1[i] <= part2[j]:
            combined.append(part1[i])
            i += 1
        else:
            combined.append(part2[j])
            j += 1

    combined.extend(part1[i:])
    combined.extend(part2[j:])

    return combined