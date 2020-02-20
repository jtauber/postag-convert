CASE_V = r"(?P<case>[NAVGD])"
CASE = r"(?P<case>[NAGD])"
GENDER = r"(?P<gender>[FMN])"
GENDER_ = r"(?P<gender>[-FMN])"
PERSON = r"(?P<person>[123])"
NUMBER = r"(?P<number>[SP])"
VOICE = r"(?P<voice>[AMP])"
TENSE = r"(?P<tense>[PIFAXY])"
TENSE_1 = r"(?P<tense>[PFAX])"
MOOD_F = r"(?P<mood>[DISO])"
MOOD_N = r"(?P<mood>N)"
MOOD_P = r"(?P<mood>P)"
DEGREE_ = r"(?P<degree>[-CS])"

POS_D = r"(?P<pos>D-)"
POS_A = r"(?P<pos>A-)"
POS_N = r"(?P<pos>N-)"
POS_V = r"(?P<pos>V-)"

# C-: conjunction
# I-: interjection
# P-: preposition
# X-: particle
POS_INDECL = r"(?P<pos>[CIPX]-)"

# RA: article
# RD: demonstrative
# RI: indefinite/interrogative pronoun
# RP: personal pronoun
# RR: relative pronoun
POS_R = r"(?P<pos>R[ADIPR])"

CNG = f"{CASE}{NUMBER}{GENDER_}"
CNG_V = f"{CASE_V}{NUMBER}{GENDER}"

REGEXES = [
    f"{POS_INDECL} --------",

    f"{POS_D} -------{DEGREE_}",

    f"{POS_A} ----{CNG_V}{DEGREE_}",
    f"{POS_N} ----{CNG_V}-",
    f"{POS_R} ----{CNG}-",

    f"{POS_V} {PERSON}{TENSE}{VOICE}{MOOD_F}-{NUMBER}--",
    f"{POS_V} -{TENSE_1}{VOICE}{MOOD_N}----",
    f"{POS_V} -{TENSE_1}{VOICE}{MOOD_P}{CNG_V}-",
]
