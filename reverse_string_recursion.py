
def reverse(string: str) -> str:
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]


if __name__ == '__main__':
    print(reverse("Vesino"))  # oniseV
