def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word:
        high_index = len(word) - 1
        low_index = 0

        for letter in word:
            if word[low_index] == word[high_index]:
                low_index += 1
                high_index -= 1
            else:
                return False

        return True
    else:
        return False
