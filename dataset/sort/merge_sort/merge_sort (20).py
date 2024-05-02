def sort_merge(sequence):
    if not sequence:
        return []

    if len(sequence) == 1:
        return sequence

    middle = len(sequence) // 2
    first_half = sequence[:middle]
    second_half = sequence[middle:]

    first_half = sort_merge(first_half)
    second_half = sort_merge(second_half)

    return merge(first_half, second_half)

def merge(part1, part2):
    result = []
    i, j = 0, 0

    while i < len(part1) and j < len(part2):
        if part1[i] <= part2[j]:
            result.append(part1[i])
            i += 1
        else:
            result.append(part2[j])
            j += 1

    result.extend(part1[i:])
    result.extend(part2[j:])

    return result