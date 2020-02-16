#!/usr/bin/env python3

import glob
import re

from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES


MAPPINGS = {
    "case": {
        1: {  # nominative
            "morphgnt2": "N",
        },
        2: {  # accusative
            "morphgnt2": "A",
        },
        3: {  # vocative
            "morphgnt2": "V",
        },
        4: {  # genitive
            "morphgnt2": "G",
        },
        5: {  # dative
            "morphgnt2": "D",
        },
        6: {  # strong ("core")
            "morphgnt2": "C",
        },
        7: {  # weak
        },
    },
    "gender": {
        1: {  # feminine
            "morphgnt2": "F",
        },
        2: {  # masculine
            "morphgnt2": "M",
        },
        3: {  # neuter
            "morphgnt2": "N",
        },
        4: {  # feminine+masculine+neuter syncretism
            "morphgnt2": "X",
        },
        5: {  # masculine+neuter (non-feminine) syncretism
            "morphgnt2": "Y",
        },
        6: {  # feminine+masculine (animate) syncretism
            "morphgnt2": "Z",
        },
    },
    "number": {
        1: {  # singular
            "morphgnt2": "S",
        },
        3: {  # plural
            "morphgnt2": "P",
        },
    },
    "person": {
        1: {  # first
            "morphgnt2": "1",
        },
        2: {  # second
            "morphgnt2": "2",
        },
        3: {  # third
            "morphgnt2": "3",
        },
    },
    "voice": {
        1: {  # active
            "morphgnt2": "A",
        },
        2: {  # middle ("MP1")
            "morphgnt2": "M",
        },
        3: {  # "passive" ("MP2")
            "morphgnt2": "P",
        },
    },
    "tense": {
        1: {  # present
            "morphgnt2": "P",
        },
        2: {  # imperfect
            "morphgnt2": "I",
        },
        3: {  # future
            "morphgnt2": "F",
        },
        4: {  # aorist
            "morphgnt2": "A",
        },
        5: {  # perfect
            "morphgnt2": "X",
        },
        6: {  # pluperfect
            "morphgnt2": "Y",
        },
        7: {  # future perfect
        },
    },
    "mood": {
        1: {  # indicative
            "morphgnt2": "I",
        },
        2: {  # imperative
            "morphgnt2": "D",
        },
        3: {  # subjunctive
            "morphgnt2": "S",
        },
        4: {  # optative
            "morphgnt2": "O",
        },
        5: {  # infinitive
            "morphgnt2": "N",
        },
        6: {  # participle
            "morphgnt2": "P",
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


def parse_and_map(scheme, regexes, postag):
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
            print(postag, parse_and_map(scheme, regexes, postag))


test_parse("morphgnt2", MORPHGNT2_REGEXES, "examples/morphgnt2.txt")
