
from itertools import cycle


def encode(message, key):
    acc = ""

    for c in message:
        x = ord(c)
        f = x + key

        nc = chr(f)
        acc = acc + nc
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


    return acc3

def split(word):
    for char in word:
        return char