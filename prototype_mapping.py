#!/usr/bin/env python3

import glob
import re

from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES


MAPPINGS = {
    "number": {
        1: {
            "morphgnt2": "S",
        },
        3: {
            "morphgnt2": "P",
        },
    },
    "person": {
        1: {
            "morphgnt2": "1",
        },
        2: {
            "morphgnt2": "2",
        },
        3: {
            "morphgnt2": "3",
        },
    },
}

REVERSE_MAPPINGS = {}

for property in MAPPINGS:
    for node in MAPPINGS[property]:
        for scheme, value in MAPPINGS[property][node].items():
            REVERSE_MAPPINGS.setdefault(scheme, {}).setdefault(property, {})[value] = node


def map_features(d, scheme):
    return {
        property: value
        for property, value in [
            (property,  REVERSE_MAPPINGS[scheme][property].get(value))
            for property, value in d.items()
        ]
        if value
    }


def parse(scheme, regexes, postag):
    for regex in regexes:
        if m := re.match(regex + "$", postag):
            d = m.groupdict()
            break
    else:
        return {}

    return map_features(d, scheme)


def test_parse(scheme, regexes, test_filename):
    with open(test_filename) as f:
        for line in f:
            postag = line.strip()
            print(postag, parse(scheme, regexes, postag))


test_parse("morphgnt2", MORPHGNT2_REGEXES, "examples/morphgnt2.txt")
