#!/usr/bin/env python3

import re


RED = "\x1b[38;5;1m"
RESET = "\x1b[0m"

def follow(a, b):
    try:
        return int(a) == int(b) + 1
    except:
        return False


FILENAMES = [
    "xml/introduction.xml",

    "xml/chapter01.xml",
    "xml/chapter02.xml",
    "xml/chapter03.xml",
    "xml/chapter04.xml",
    "xml/chapter05.xml",
    "xml/chapter06.xml",
    "xml/chapter07.xml",
    "xml/chapter08.xml",
    "xml/chapter09.xml",
    "xml/chapter10.xml",
    "xml/chapter11.xml",
    "xml/chapter12.xml",
    "xml/chapter13.xml",
    "xml/chapter14.xml",
    "xml/chapter15.xml",
    "xml/chapter16.xml",

    "xml/ulfilas.xml",

    "xml/matthew.xml",
    "xml/mark.xml",
    "xml/luke.xml",
    "xml/john.xml",
    "xml/timothy.xml",

]

prev_pgn = None

for filename in FILENAMES:
    data = open(filename).read()

    print(filename, end=": ")
    for m in re.finditer("<pb n=\"([^\"]+)\"/>", data):
        pgn = m.group(1)
        if prev_pgn is None or follow(pgn, prev_pgn):
            print(pgn, end=" ")
        else:
            print(f"{RED}{pgn}{RESET}", end=" ")
        prev_pgn = pgn
    print()