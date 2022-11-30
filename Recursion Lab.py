def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)


def cat_ears(n):
    if n == 0:
        return 0
    else:
        return 2 + cat_ears(n - 1)


def alien_ears(n):
    if n == 0:
        return n
    else:
        if n % 2 == 0:
            return 3 + alien_ears(n - 1)
        else:
            return 2 + alien_ears(n - 1)


def main():
    print(power(2, 3))
    print(power(-2, 3))
    print(power(1, 5))
    print('----------------')
    print(cat_ears(0))
    print(cat_ears(1))
    print(cat_ears(2))
    print('----------------')
    print(alien_ears(1))
    print(alien_ears(2))


if __name__ == '__main__':
    main()
