def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)


def add_fact(n):
    print('step {0}'.format(n))
    if n == 0:
        return 0

    return n + add_fact(n - 1)


def sum_func(n):
    if n == 0:
        return 0

    return (n % 10) + sum_func(int(n / 10))


# TODO
def word_split(phrase, list_of_words, output=None):
    pass
