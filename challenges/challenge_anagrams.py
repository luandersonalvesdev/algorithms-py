def bubble_sort(str_list):
    n = len(str_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if str_list[j] > str_list[j + 1]:
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]

def are_anagrams(first_string, second_string):
    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if len(first_string) != len(second_string):
        return False

    str1_list = list(first_string)
    str2_list = list(second_string)

    bubble_sort(str1_list)
    bubble_sort(str2_list)

    return str1_list == str2_list

def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    are_anagrams_result = are_anagrams(first_string, second_string)

    str1_sorted = list(first_string)
    str2_sorted = list(second_string)
    bubble_sort(str1_sorted)
    bubble_sort(str2_sorted)

    return ("".join(str1_sorted), "".join(str2_sorted), are_anagrams_result)