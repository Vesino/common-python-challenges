"""
    Obtain the missing numbers in a list [1...100]
"""


def get_missing_numbers(lst: list) -> list:
    if type(lst) != list:
        raise TypeError(f'{lst} is not a list')

    if len(lst) > 100 or len(lst) <= 0:
        raise ValueError('Len of list argument invalid')

    missing_numbers = []
    for number in range(100)[1:]:
        if number not in lst:
            missing_numbers.append(number)

    return missing_numbers


if __name__ == '__main__':
    lst = list(range(100))
    lst.pop(50)
    lst.pop(22)
    print(get_missing_numbers(lst))  # [22, 50]
    print(get_missing_numbers(list(range(1000))))  # ValueError: Len of list argument invalid
