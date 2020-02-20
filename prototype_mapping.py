#!/usr/bin/env python3

import glob
import re

from patterns.morphgnt import REGEXES as MORPHGNT1_REGEXES
from patterns.morphgnt2 import REGEXES as MORPHGNT2_REGEXES
from patterns.morpheus import REGEXES1 as MORPHEUS1_REGEXES


REGEXES = {
    "morphgnt1": MORPHGNT1_REGEXES,
    "morphgnt2": MORPHGNT2_REGEXES,
    "morpheus1": MORPHEUS1_REGEXES,
}


MAPPINGS = {
    "pos": {
        1: {  # adjective
            "morpheus1": ("a", True),
            "morphgnt1": ("A", True),
        },
        2: {  # conjunction
            "morpheus1": ("c", True),
            "morphgnt1": ("C", True),
        },
        3: {  # adverb
            "morpheus1": ("d", True),
        },
        4: {  # particle
            "morpheus1": ("g", True),
        },
        5: {  # interjection
            "morpheus1": ("i", True),
        },
        6: {  # definite article
            "morpheus1": ("l", True),
        },
        7: {  # numeral
            "morpheus1": ("m", True),
        },
        8: {  # noun
            "morpheus1": ("n", True),
        },
        9: {  # pronoun
            "morpheus1": ("p", True),
        },
        10: {  # preposition
            "morpheus1": ("r", True),
        },
        11: {  # punctuation
            "morpheus1": ("u", True),
        },
        12: {  # verb
            "morpheus1": ("v", True),
        },
        13: {  # ???
            "morpheus1": ("x", True),
        },
    },
    "case": {
        1: {  # nominative
            "morphgnt1": ("N", True),
            "morphgnt2": ("N", True),
            "morpheus1": ("n", True),
        },
        2: {  # accusative
            "morphgnt1": ("A", True),
            "morphgnt2": ("A", True),
            "morpheus1": ("a", True),
        },
        3: {  # vocative
            "morphgnt1": ("V", True),
            "morphgnt2": ("V", True),
            "morpheus1": ("v", True),
        },
        4: {  # genitive
            "morphgnt1": ("G", True),
            "morphgnt2": ("G", True),
            "morpheus1": ("g", True),
        },
        5: {  # dative
            "morphgnt1": ("D", True),
            "morphgnt2": ("D", True),
            "morpheus1": ("d", True),
        },
        6: {  # strong ("core")
            "morphgnt2": ("C", True),
        },
        7: {  # weak
        },
    },
    "gender": {
        1: {  # feminine
            "morphgnt1": ("F", True),
            "morphgnt2": ("F", True),
            "morpheus1": ("f", True),
        },
        2: {  # masculine
            "morphgnt1": ("M", True),
            "morphgnt2": ("M", True),
            "morpheus1": ("m", True),
        },
        3: {  # neuter
            "morphgnt1": ("N", True),
            "morphgnt2": ("N", True),
            "morpheus1": ("n", True),
        },
        4: {  # feminine+masculine+neuter syncretism
            "morphgnt2": ("X", True),
        },
        5: {  # masculine+neuter (non-feminine) syncretism
            "morphgnt2": ("Y", True),
        },
        6: {  # feminine+masculine (animate) syncretism
            "morphgnt2": ("Z", True),
        },
    },
    "number": {
        1: {  # singular
            "morphgnt1": ("S", True),
            "morphgnt2": ("S", True),
            "morpheus1": ("s", True),
        },
        2: {  # dual
            "morpheus1": ("d", True),
        },
        3: {  # plural
            "morphgnt1": ("P", True),
            "morphgnt2": ("P", True),
            "morpheus1": ("p", True),
        },
    },
    "person": {
        1: {  # first
            "morphgnt1": ("1", True),
            "morphgnt2": ("1", True),
            "morpheus1": ("1", True),
        },
        2: {  # second
            "morphgnt1": ("2", True),
            "morphgnt2": ("2", True),
            "morpheus1": ("2", True),
        },
        3: {  # third
            "morphgnt1": ("3", True),
            "morphgnt2": ("3", True),
            "morpheus1": ("3", True),
        },
    },
    "voice": {
        1: {  # active
            "morphgnt1": ("A", True),
            "morphgnt2": ("A", True),
            "morpheus1": ("a", True),
        },
        2: {  # middle ("MP1")
            "morphgnt1": ("M", True),
            "morphgnt2": ("M", True),
            "morpheus1": ("m", True),
        },
        3: {  # "passive" ("MP2")
            "morphgnt1": ("P", True),
            "morphgnt2": ("P", True),
            "morpheus1": ("p", True),
        },
        4: {
            "morpheus1": ("e", True),
            "morphgnt1": ("M", True),
            "morphgnt2": ("M", False),
        }
    },
    "tense": {
        1: {  # present
            "morphgnt1": ("P", True),
            "morphgnt2": ("P", True),
            "morpheus1": ("p", True),
        },
        2: {  # imperfect
            "morphgnt1": ("I", True),
            "morphgnt2": ("I", True),
            "morpheus1": ("i", True),
        },
        3: {  # future
            "morphgnt1": ("F", True),
            "morphgnt2": ("F", True),
            "morpheus1": ("f", True),
        },
        4: {  # aorist
            "morphgnt1": ("A", True),
            "morphgnt2": ("A", True),
            "morpheus1": ("a", True),
        },
        5: {  # perfect
            "morphgnt1": ("X", True),
            "morphgnt2": ("X", True),
            "morpheus1": ("r", True),
        },
        6: {  # pluperfect
            "morphgnt1": ("Y", True),
            "morphgnt2": ("Y", True),
            "morpheus1": ("l", True),
        },
        7: {  # future perfect
            "morpheus1": ("t", True),
        },
    },
    "mood": {
        1: {  # indicative
            "morphgnt1": ("I", True),
            "morphgnt2": ("I", True),
            "morpheus1": ("i", True),
        },
        2: {  # imperative
            "morphgnt1": ("D", True),
            "morphgnt2": ("D", True),
            "morpheus1": ("m", True),
        },
        3: {  # subjunctive
            "morphgnt1": ("S", True),
            "morphgnt2": ("S", True),
            "morpheus1": ("s", True),
        },
        4: {  # optative
            "morphgnt1": ("O", True),
            "morphgnt2": ("O", True),
            "morpheus1": ("o", True),
        },
        5: {  # infinitive
            "morphgnt1": ("N", True),
            "morphgnt2": ("N", True),
            "morpheus1": ("n", True),
        },
        6: {  # participle
            "morphgnt1": ("P", True),
            "morphgnt2": ("P", True),
            "morpheus1": ("p", True),
        },
    },
    "degree": {
        1: {  # comparative
            "morpheus1": ("c", True),
            "morphgnt1": ("C", True),
        },
        2: {  # superlative
            "morpheus1": ("s", True),
            "morphgnt1": ("S", True),
        },
    }
}

REVERSE_MAPPINGS = {}

for property in MAPPINGS:
    for node in MAPPINGS[property]:
        for scheme, value in MAPPINGS[property][node].items():
            if value[1]:
                REVERSE_MAPPINGS.setdefault(scheme, {}).setdefault(property, {})[value[0]] = node


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
            (property,  MAPPINGS[property][value].get(scheme, (None,))[0])
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


def test_mapping(test_filename, scheme_in, scheme_out):
    with open(test_filename) as f:
        for line in f:
            postag = line.strip()
            features = parse_and_map(scheme_in, REGEXES[scheme_in], postag)
            postag2 = reverse_map_and_render(scheme_out, features)
            print(postag, features, postag2)


# test_mapping("examples/morphgnt2.txt", "morphgnt2", "morpheus1")
# test_mapping("examples/morpheus-celano-shorter.txt", "morpheus1", "morphgnt2")
test_mapping("examples/morphgnt.txt", "morphgnt1", "morphgnt2")
