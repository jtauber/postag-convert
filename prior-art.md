# Prior Art

Previous code I've written to do this in various places.

## MorphGNT API string to dict

<https://github.com/morphgnt/morphgnt-api/blob/f53c7b4243f9da964f4dd2901544265f3ba8f465/morphgnt_api/models.py#L7>

## Diorsis to my own compact form

<https://github.com/jtauber/enchiridion/blob/b1115d8fd5f4d01d41ab077405b9a24b94c07088/merge.py#L9>

## ccat conversion in greek-inflexion

<https://github.com/jtauber/greek-inflexion/blob/3f031da54d2d7ac90ecf11693c770863fe66252e/morphgnt_utils.py#L13>

## lxxmorph conversion in greek-inflexion

<https://github.com/jtauber/greek-inflexion/blob/3f031da54d2d7ac90ecf11693c770863fe66252e/lxxmorph_utils.py#L25>

## Other Code

### CCAT to MorphGNT

2010 code for converting between original 1993 CCAT greekmrp format to fixed-width format started using in late 90s:

```
parse = list("--------")

pos = morph.split()[0]
if " " in morph:
    attr = morph.split()[1]

if pos in ["N", "RA", "RP", "RR", "A", "RD", "RI"]:
    parse[4:4+len(attr)] = attr
elif pos in ["V"]:
    if len(attr) == 5:
        parse[0] = attr[3]
        parse[1:4] = attr[0:3]
        parse[5] = attr[4]
    elif len(attr) == 6:
        parse[1:7] = attr
    elif len(attr) == 3:
        parse[1:4] = attr
    else:
        raise morph
elif pos in ["C", "P", "D", "X", "I"]:
    pass
else:
    raise morph

parse = "".join(parse)
```

### DeepMorphology

```
def human_pos(pos):
    return {
        "a-": "ADJ",
        "ae": "PROP.ADJ",
        "c-": "CONJ",
        "d-": "ADV",
        "dd": "ADV?",
        "de": "ADV?",
        "di": "ADV?",
        "dr": "ADV?",
        "dx": "ADV?",
        "g-": "PTCL",
        "gm": "MODAL.PTCL",
        "i-": "INTJ",
        "l-": "ART",
        "m-": "NUM",
        "n-": "NOUN",
        "ne": "PROP.NOUN",
        "p-": "PRONOUN",
        "pa": "PRONOUN?",
        "pc": "PRONOUN?",
        "pd": "PRONOUN?",
        "pi": "PRONOUN?",
        "pp": "PRONOUN?",
        "pr": "PRONOUN?",
        "ps": "PRONOUN?",
        "px": "PRONOUN?",
        "r-": "PREP",
        "u-": "PUNC",
        "v-": "VERB",
        "vc": "COPULA",
    }.get(pos, pos)

```def human_parse(parse):
    if len(parse) == 8:
        if parse == "--------":
            return "INDECL"
        else:
            person = {
                "-": None,
            }.get(parse[0], parse[0])
            number = {
                "s": "SG",
                "d": "DU",
                "p": "PL",
                "-": None,
            }.get(parse[1], parse[1])
            tense = {
                "p": "PRES",
                "i": "IMPRF",
                "f": "FUT",
                "a": "AOR",
                "r": "PRF",
                "l": "PLPRF",
                "-": None,
            }.get(parse[2], parse[2])
            mood = {
                "i": "IND",
                "m": "IMP",
                "n": "INF",
                "s": "SBJV",
                "o": "OPT",
                "p": "PTCP",
                "-": None,
            }.get(parse[3], parse[3])
            voice = {
                "a": "ACT",
                "m": "MID",
                "e": "MID",
                "p": "PASS",
            }.get(parse[4], parse[4])
            gender = {
                "m": "M",
                "f": "F",
                "n": "N",
                "-": None,
            }.get(parse[5], parse[5])
            case = {
                "n": "NOM",
                "a": "ACC",
                "g": "GEN",
                "d": "DAT",
                "v": "VOC",
                "-": None,
            }.get(parse[6], parse[6])
            degree = {
                "c": "COMP",  # @@@
                "s": "SUP",  # @@@
                "-": None,
            }.get(parse[7], parse[7])
            if case and tense:
                if mood != "PTCP":
                    return f"@1@ {parse}"
                return f"{tense} {voice} {case}.{number} {gender} {mood}"
            elif case and not tense:
                if degree:
                    return f"{case}.{number} {gender} {degree}"
                if gender:
                    return f"{case}.{number} {gender}"
                else:
                    return f"{case}.{number}"
            elif tense and not case:
                if person:
                    return f"{tense} {voice} {person}{number} {mood}"
                elif mood == "INF":
                    return f"{tense} {voice} {mood}"
                else:
                    return f"@@@ {parse}"
            else:
                return f"@@@ {parse}"
    else:
        return "UNKNOWN"
```

### greek-verb-form-classes

```
tense_voice = key[0:2]
if key[2] == "N":
    person_number = "INF"
elif key[2] == "I":
    person_number = key[4] + key[5] + {"S": "G", "P": "L"}[key[5]]
else:
    continue
```
