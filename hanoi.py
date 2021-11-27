"""
    Calculate Hanoi movements recursively.
"""


def move(f: str, t: str):
    """
    :param f: stands for From
    :param t: stands for To
    :return: None
    """
    print("Move disc from {} to {}".format(f, t))


def hanoi(n: int, f: str, h: str, t: str):
    """

    :param n: number of disks
    :param f: from
    :param h: helper (or move via)
    :param t: target
    :return: None
    """
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)


if __name__ == '__main__':
    hanoi(4, "A", "B", "C")
    """
        Move disc from A to B
        Move disc from A to C
        Move disc from B to C
        Move disc from A to B
        Move disc from C to A
        Move disc from C to B
        Move disc from A to B
        Move disc from A to C
        Move disc from B to C
        Move disc from B to A
        Move disc from C to A
        Move disc from B to C
        Move disc from A to B
        Move disc from A to C
        Move disc from B to C
    """