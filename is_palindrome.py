
def is_palindrome(string: str) -> bool:
    if type(string) != str:
        raise TypeError(f'{string} is not str')

    string = string.replace(' ', '')
    return string.lower() == string[::-1].lower()


if __name__ == '__main__':
    my_palindrome = 'Anita lava la tina'
    print(is_palindrome(my_palindrome))  # True
    print(is_palindrome('Bob'))  # True
    print(is_palindrome('This is not a palindrome'))  # True
    print(is_palindrome(['cjfe', 8]))  # TypeError: ['cjfe', 8] is not str
