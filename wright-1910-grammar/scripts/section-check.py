#!/usr/bin/env python3

import re


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

prev_section = None

for filename in FILENAMES:
    data = open(filename).read()

    print(filename, end=": ")
    for m in re.finditer("<div type=\"section\" n=\"([^\"]+)\"", data):
        section = int(m.group(1))
        print(section, end=" ")
        assert prev_section is None or section == prev_section + 1
        prev_section = section
    print()