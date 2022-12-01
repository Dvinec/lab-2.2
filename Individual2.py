#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))

    x = abs(a)
    if x >= 4:
        print("Модуль числа a не меньше 4")

    y = abs(b)
    if y >= 4:
        print("Модуль числа b не меньше 4")


    z = abs(c)
    if z >= 4:
        print("Модуль числа с не меньше 4")
        exit(1)