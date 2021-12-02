"""
    Compute the n Fibonacci number
"""

cache = {0: 0, 1: 1}


def compute_fibonacci(n: int):
    if type(n) != int:
        raise TypeError
    if n in cache:
        return cache[n]
    cache[n] = compute_fibonacci(n - 1) + compute_fibonacci(n - 2)
    return cache[n]


if __name__ == '__main__':
    print(compute_fibonacci(15))
