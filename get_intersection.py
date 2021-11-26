"""
    Given two list, find the intersections
"""


def get_intersection(lst1: list, lst2: list) -> list:
    if type(lst1) != list or type(lst2) != list:
        raise TypeError('Arguments should be of type List')

    return list(set(lst1) & set(lst2))


if __name__ == '__main__':
    students_in_math_class = [
        "Max",
        "Raul",
        "Ximena",
        "Hobbit",
        "David",
        "Mariana"
    ]
    students_in_philosophy_class = [
        "Ximena",
        "Hobbit",
        "David",
        "Rodrigo",
        "Alejandro",
        "Daniela"
    ]
    # Show students in both classes
    print(get_intersection(students_in_math_class, students_in_philosophy_class))  # ['Ximena', 'Hobbit', 'David']

    print(get_intersection('Un string', ['List of on string']))  # TypeError: Arguments should be of type List
