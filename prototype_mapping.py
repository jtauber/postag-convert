#!/usr/bin/env python3

import glob
import re

from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES
from patterns.morpheus import REGEXES1 as MORPHEUS1_REGEXES


MAPPINGS = {
    "pos": {
        1: {  # adjective
            "morpheus1": "a",
        },
        2: {  # conjunction
            "morpheus1": "c",
        },
        3: {  # adverb
            "morpheus1": "d",
        },
        4: {  # particle
            "morpheus1": "g",
        },
        5: {  # interjection
            "morpheus1": "i",
        },
        6: {  # definite article
            "morpheus1": "l",
        },
        7: {  # numeral
            "morpheus1": "m",
        },
        8: {  # noun
            "morpheus1": "n",
        },
        9: {  # pronoun
            "morpheus1": "p",
        },
        10: {  # preposition
            "morpheus1": "r",
        },
        11: {  # punctuation
            "morpheus1": "u",
        },
        12: {  # verb
            "morpheus1": "v",
        },
        13: {  # ???
            "morpheus1": "x",
        },
    },
    "case": {
        1: {  # nominative
            "morphgnt2": "N",
            "morpheus1": "n",
        },
        2: {  # accusative
            "morphgnt2": "A",
            "morpheus1": "a",
        },
        3: {  # vocative
            "morphgnt2": "V",
            "morpheus1": "v",
        },
        4: {  # genitive
            "morphgnt2": "G",
            "morpheus1": "g",
        },
        5: {  # dative
            "morphgnt2": "D",
            "morpheus1": "d",
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
            "morpheus1": "f",
        },
        2: {  # masculine
            "morphgnt2": "M",
            "morpheus1": "m",
        },
        3: {  # neuter
            "morphgnt2": "N",
            "morpheus1": "n",
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
            "morpheus1": "s",
        },
        2: {  # dual
            "morpheus1": "d",
        },
        3: {  # plural
            "morphgnt2": "P",
            "morpheus1": "p",
        },
    },
    "person": {
        1: {  # first
            "morphgnt2": "1",
            "morpheus1": "1",
        },
        2: {  # second
            "morphgnt2": "2",
            "morpheus1": "2",
        },
        3: {  # third
            "morphgnt2": "3",
            "morpheus1": "3",
        },
    },
    "voice": {
        1: {  # active
            "morphgnt2": "A",
            "morpheus1": "a",
        },
        2: {  # middle ("MP1")
            "morphgnt2": "M",
            "morpheus1": "m",
        },
        3: {  # "passive" ("MP2")
            "morphgnt2": "P",
            "morpheus1": "p",
        },
        4: {
            "morpheus1": "e",  # @@@
        }
    },
    "tense": {
        1: {  # present
            "morphgnt2": "P",
            "morpheus1": "p",
        },
        2: {  # imperfect
            "morphgnt2": "I",
            "morpheus1": "i",
        },
        3: {  # future
            "morphgnt2": "F",
            "morpheus1": "f",
        },
        4: {  # aorist
            "morphgnt2": "A",
            "morpheus1": "a",
        },
        5: {  # perfect
            "morphgnt2": "X",
            "morpheus1": "r",
        },
        6: {  # pluperfect
            "morphgnt2": "Y",
            "morpheus1": "l",
        },
        7: {  # future perfect
            "morpheus1": "t",
        },
    },
    "mood": {
        1: {  # indicative
            "morphgnt2": "I",
            "morpheus1": "i",
        },
        2: {  # imperative
            "morphgnt2": "D",
            "morpheus1": "m",
        },
        3: {  # subjunctive
            "morphgnt2": "S",
            "morpheus1": "s",
        },
        4: {  # optative
            "morphgnt2": "O",
            "morpheus1": "o",
        },
        5: {  # infinitive
            "morphgnt2": "N",
            "morpheus1": "n",
        },
        6: {  # participle
            "morphgnt2": "P",
            "morpheus1": "p",
        },
    },
    "degree": {
        1: {  # comparative
            "morpheus1": "c",
        },
        2: {  # superlative
            "morpheus1": "s",
        },
    }
}

REVERSE_MAPPINGS = {}

for property in MAPPINGS:
    for node in MAPPINGS[property]:
        for scheme, value in MAPPINGS[property][node].items():
            REVERSE_MAPPINGS.setdefault(scheme, {}).setdefault(property, {})[value] = node


def map_features(features, scheme):
    return {
        property: value
        for property, value in [
            (property,  REVERSE_MAPPINGS[scheme][property].get(value))
            for property, value in features.items()
        ]
        if value
    }


def reverse_map_features(features, scheme):
    return {
        property: value
        for property, value in [
            (property,  MAPPINGS[property][value].get(scheme))
            for property, value in features.items()
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


def render(scheme, features):
    if scheme == "morphgnt2":
        return "".join(
            features.get(property, "-")
            for property in [
                "tense", "voice", "mood", "person", "case", "number", "gender"
            ]
        )
    if scheme == "morpheus1":
        return "".join(
            features.get(property, "-")
            for property in [
                "pos", "person", "number", "tense", "mood",
                "voice", "gender", "case", "degree",
            ]
        )


def reverse_map_and_render(scheme, features):
    return render(scheme, reverse_map_features(features, scheme))


def test_mapping(scheme, regexes, test_filename):
    with open(test_filename) as f:
        for line in f:
            postag = line.strip()
            features = parse_and_map(scheme, regexes, postag)
            postag2 = reverse_map_and_render(scheme, features)
            print(postag, features, postag2)
            assert postag == postag2


# test_mapping("morphgnt2", MORPHGNT2_REGEXES, "examples/morphgnt2.txt")
test_mapping("morpheus1", MORPHEUS1_REGEXES, "examples/morpheus-celano-shorter.txt")
