"""
    Find pairs of integers in list so that their sum is equal to the given number x
"""


def find_pairs(lista: list, number: int) -> list:
    if not all([type(number) == int for number in lista]):
        raise TypeError(f'{lista} is not a list of int')

    pairs = []
    for index, element_1 in enumerate(lista):
        for new_index, element_2 in enumerate(lista[index+1:]):
            if element_1 + element_2 == number:
                pairs.append((element_1, element_2))
    return pairs


if __name__ == '__main__':
    my_list = [1, 2, 3, 5]
    print(find_pairs(my_list, 8))  # [(3, 5)]
    my_other_list = [3, 1, 2, 5]
    print(find_pairs(my_other_list, 6))  # [(1, 5)]
    my_new_list = [3, 2, 1, 2, 5, -1]
    print(find_pairs(my_new_list, 4))  # [(3, 1), (2, 2), (5, -1)]

    # Error:
    my_new_list = [3, 2, "python", 1, 2, 5, -1]
    print(find_pairs(my_new_list, 4))  # Exception: TypeError: [3, 2, 'python', 1, 2, 5, -1] is not a list of int
