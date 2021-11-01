#!/usr/bin/env python


def cel(fah):
    return ((fah - 32) * 5) / 9


def fah(cel):
    return ((cel * 9) / 5) + 32


if __name__ == '__main__':
    print(cel(98.6))
    print(cel(37.0))
    print(fah(98.6))
    print(fah(37.0))
