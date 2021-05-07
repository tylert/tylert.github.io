#!/usr/bin/env python


def celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9


def fahrenheit(celsius):
    return ((celsius * 9) / 5) + 32


if __name__ == '__main__':
    print(celsius(98.6))
    print(celsius(37))
    print(fahrenheit(98.6))
    print(fahrenheit(37))
