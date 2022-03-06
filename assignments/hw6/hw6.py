"""
Name: <Josh>
Partner: <Josh>
<workhorse>.py
"""
import itertools as it
from itertools import *
import binascii
import math

def main():
    # add function calls here

    print(sum_n(5))
    print(sum_n_cubes(5))
    print(sphere_area(5))
    print(sphere_volume(5))

    pass






def encode(message, key):
    acc = ""

    for c in message:
        x = ord(c)
        f = x + key
        print(f)
        nc = chr(f)
        acc = acc + nc
    return acc



def cash_converter():

    x = eval(input("Enter the dollar value of your money: "))

    print("$" + "{: .2f}".format(x))


def sphere_area(radius):

    Area = 4 * math.pi * radius ** 2

    return Area


def sphere_volume(radius):

    volume = (4/3) * math.pi * radius ** 3

    return volume


def sum_n(n):

    acc = 0

    for i in range(n):
        total = i + acc
        acc = acc + total

    return acc


def sum_n_cubes(n):

    acc = 0

    for i in range(n):
        total = i ** 3 + acc
        acc = acc + total

    return acc

def encode_better(message, key):

    message = message.replace(" ", "")
    message = message.upper()
    message = split(message)
    key = key.upper()
    key = split(key)
    alist = []
    blist = []
    clist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    for i in message:
        i = ord(str(i))
        ascii = i - 65
        alist.append(ascii)


    for e in key:
        e = ord(str(e))
        ascii2 = e - 65
        blist.append(ascii2)


    acc3 = ""

    for (l, n) in zip(alist, cycle(blist)):
        if l + n > 25:
            ky = (clist[(l + n) - 26])
            keyword = ky + 64
            acc3 = chr(keyword) + acc3
        elif l + n <= 25:
            code = l + n + 65
            acc3 = chr(code) + acc3

    acc3 = acc3[::-1]
    return acc3

def split(word):
    for char in word:
        return char

main()

if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
