def check_if_word_has_4_or_more_letters(word):
    return len(word) >= 4


def check_what_number_is_greater(first_number, second_number):
    if first_number > second_number:
        result = first_number
    else:
        result = second_number
    return result


def check_if_number_is_odd_or_even(number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return result


def check_if_element_exists_in_list(element, input_list):
    return element in input_list
