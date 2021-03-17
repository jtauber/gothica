#!/usr/bin/env python3

import collections
import glob
import unicodedata


counter = collections.Counter()

for filename in sorted(glob.glob("xml/chapter??.xml")):
    for line in open(filename):
        glyph_cluster = None
        for char in unicodedata.normalize("NFD", line):
            if unicodedata.category(char)[0] == "M":
                if glyph_cluster is None:
                    raise Exception
                else:
                    glyph_cluster += char
            else:
                if glyph_cluster is None:
                    glyph_cluster = char
                else:
                    counter[glyph_cluster] += 1
                    glyph_cluster = char
        counter[glyph_cluster] += 1



for glyph_cluster, count in sorted(counter.items()):
    print()
    if glyph_cluster.isprintable():
        print(f"{glyph_cluster:50s} {count:>6d}")
    else:
        print(f"{'':50s} {count:>6d}")
    for char in glyph_cluster:
        print(f"\t{ord(char):05X} {unicodedata.category(char)} {unicodedata.name(char, '?'):60s}")
