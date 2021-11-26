
def is_anagram(s1: str, s2: str) -> bool:
    s1, s2 = s1.lower(), s2.lower()
    return set(s1) == set(s2)

if __name__ == '__main__':
    print(is_anagram('elvis', 'lives'))
    print(is_anagram('Jim Morrison', 'Mojo Rrisin'))
