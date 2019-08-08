'''
Run-length encoding is a fast and simple method of encoding strings.

The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.

You can assume the string to be encoded have no digits and consists solely of alphabetic characters.

You can assume the string to be decoded is valid.
'''

from itertools import groupby


def decode(string):
    return ''.join(letter * int(num) for num, letter in zip(string[::2], string[1::2]))


def encode(string):
    return ''.join(str(len(list(lst))) + letter for letter, lst in groupby(string))
