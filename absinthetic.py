#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def get(prompt='', allow_empty=False):
    try:
        r = input(prompt)
    except EOFError:
        print('')
        get(prompt)
    except KeyboardInterrupt:
        print('')
        exit()
    else:
        return r if r != '' or allow_empty else get(prompt)

###

class MultiDigitIntException(Exception):
    """Raised when a read integer is more than 1 digit long"""

def get_array(array, x):
    try:
        return array[x]
    except IndexError:
        array[x] = get()

def to_list(o, array, x, _k):
    for e in o:
        if _k in ('!', '¡'):
            print(e)                
        elif _k != '¡':
            array.append(e)
            x += 1

def to_int(s, _k):
    if _k == 'h':
        b = 16
    elif _k == 'o':
        b = 8
    elif _k == 'b':
        b = 2
    else:
        b = 10
    return int(s, b)

def dec(array, x):
    x -= 1
    return array[x]

def inc(array, x):
    x += 1
    try:
        return array[x]
    except IndexError:
        array.append(0)


def command(array, x, r, k, _k):
    cmd = {'?': get(),
           '¿': get(allow_empty=True),
           '!': print(retenue or get_array(array, x)),
           '¡': print(retenue or get_array(array, x, True)),
           '<': dec(x),
           '>': inc(x),
           '#': to_int(r or get_array(array, x), _k),
           'ŀ': to_list(get_array(array, x), array, _k),
           'ø': None,
           ',': len(array),
           'b': bin(get_array(array, x))[2:],
           'x': hex(get_array(array, x))[2:],
           'o': oct(get_array(array, x))[2:],
           '+': r + get_array(array, x),
           '-': r - get_array(array, x),
           '×': r * get_array(array, x),
           '∕': r // get_array(array, x),
           '%': r % get_array(array, x),
           '`': r ** get_array(array, x),
           '√': get(array, array, x) ** (1 / (r or 2))
           '°': 10 ** r,
           '²': 2 ** r,
           '«': get_array(array, x) << get_array(array, x + 1),
           '»': get_array(array, x) >> get_array(array, x + 1),
           '¬': ~ get_array(array, x),
           '±': - retenue,
           '&': get_array(array, x) & get_array(array, x + 1),
           '|': get_array(array, x) | get_array(array, x + 1),
           '^': get_array(array, x) ^ get_array(array, x + 1),
           }
    try:
        r = cmd[k]
    except KeyError:
        if k in '0123456789':
            r = k
            if _k in '0123456789':
                raise MultiDigitIntException
    return r

try:
    f = open(sys.argv[1])
except IndexError:
    f = sys.stdin
prog = f.read()

array = []
i = 0
index = 0
retenue = None
while i < len(prog):
    try:
        command(array, index, prog[i], prog[i + 1])
    except IndexError:
        command(array, index, prog[i], None)
    except MultiDigitIntException:
        while prog[i] in '0123456789':
            retenue += prog[i]
            i += 1
        retenue = int(retenue)
    i += 1
