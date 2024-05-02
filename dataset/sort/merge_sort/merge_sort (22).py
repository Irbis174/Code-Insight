def sort_merge(sequence):
    if len(sequence) <= 1:
        return sequence

    middle = len(sequence) // 2
    first_part = sequence[:middle]
    second_part = sequence[middle:]

    first_part = sort_merge(first_part)
    second_part = sort_merge(second_part)

    return merge(first_part, second_part, sequence)

def merge(part1, part2, result):
    i, j, k = 0, 0, 0

    while i < len(part1) and j < len(part2):
        if part1[i] <= part2[j]:
            result[k] = part1[i]
            i += 1
        else:
            result[k] = part2[j]
            j += 1
        k += 1

    while i < len(part1):
        result[k] = part1[i]
        i += 1
        k += 1

    while j < len(part2):
        result[k] = part2[j]
        j += 1
        k += 1

    return result