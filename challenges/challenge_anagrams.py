def quicksort(str_list):
    if len(str_list) <= 1:
        return str_list
    else:
        pivot = str_list[0]
        less = [x for x in str_list[1:] if x <= pivot]
        greater = [x for x in str_list[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = "".join(quicksort(list(first_string)))
    second_sorted = "".join(quicksort(list(second_string)))

    return (first_sorted, second_sorted, first_sorted == second_sorted)
