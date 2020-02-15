#!/usr/bin/env python3

import glob
import re

from patterns.robinson import REGEXES as ROBINSON_REGEXES
from patterns.morphgnt import REGEXES as MORPHGNT_REGEXES
from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES


def test_parse(regexes, test_filename):
    with open(test_filename) as f:
        for line in f:
            postag = line.strip()

            for regex in regexes:
                if m := re.match(regex + "$", postag):
                    break
            else:
                print(postag)
                quit()


test_parse(ROBINSON_REGEXES, "examples/robinson.txt")
test_parse(MORPHGNT_REGEXES, "examples/morphgnt.txt")
test_parse(MORPHGNT2_REGEXES, "examples/morphgnt2.txt")
