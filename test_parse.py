#!/usr/bin/env python3

import glob
import re

from patterns.robinson import REGEXES as ROBINSON_REGEXES
from patterns.morphgnt import REGEXES as MORPHGNT_REGEXES
from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES
from patterns.morpheus import REGEXES1 as MORPHEUS1_REGEXES
from patterns.morpheus import REGEXES2 as MORPHEUS2_REGEXES


def test_parse(label, regexes, test_filename):
    print(label, end="...", flush=True)
    count = 0
    with open(test_filename) as f:
        for line in f:
            count += 1
            postag = line.strip()

            for regex in regexes:
                if m := re.match(regex + "$", postag):
                    break
            else:
                print("ERROR.")
                print(postag)
                quit()
    print(f"{count} PASSED.")


test_parse("robinson", ROBINSON_REGEXES, "examples/robinson.txt")
test_parse("morphgnt", MORPHGNT_REGEXES, "examples/morphgnt.txt")
test_parse("morphgnt2", MORPHGNT2_REGEXES, "examples/morphgnt2.txt")
test_parse("morpheus1", MORPHEUS1_REGEXES, "examples/morpheus-celano-shorter.txt")
test_parse("morpheus2", MORPHEUS2_REGEXES, "examples/morpheus-celano.txt")
