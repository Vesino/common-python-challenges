# from collections.abc import Iterable


def find_duplicates(elements) -> list:
    # The follow statement does not check for classes that are iterable through __getitem__. like Strings
    # assert isinstance(elements, Iterable), 'The argument is not an iterable'

    # A pythonic approach is to assume an iterable
    try:
        duplicates, seen = set(), set()
        for element in elements:
            if element in seen:
                duplicates.add(element)
            seen.add(element)
        return list(duplicates)
    except TypeError as e:
        return [e]


if __name__ == '__main__':
    my_list = [1, 'Hello', 1, 3, 5, 'Hello']

    print(find_duplicates(my_list))
    print(find_duplicates(4))
    print(find_duplicates('AnA'))
