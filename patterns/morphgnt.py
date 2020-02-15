CASE_V = "[NAVGD]"
CASE = "[NAGD]"
GENDER = "[FMN]"
PERSON = "[123]"
NUMBER = "[SP]"
VOICE = "[AMP]"
TENSE = "[PIFAXY]"
TENSE_1 = "[PFAX]"
MOOD_F = "[DISO]"

CN_ = f"{CASE}{NUMBER}-"
CNG = f"{CASE}{NUMBER}{GENDER}"
CNG_V = f"{CASE_V}{NUMBER}{GENDER}"

REGEXES = [
    "C- --------",
    "I- --------",
    "P- --------",
    "X- --------",

    "D- -------[-C]",

    f"A- ----{CNG_V}[-CS]",
    f"N- ----{CNG_V}-",
    f"RA ----{CNG}-",
    f"RD ----{CNG}-",
    f"RI ----{CNG}-",
    f"RP ----{CNG}-",
    f"RP ----{CN_}-",
    f"RR ----{CNG}-",

    f"V- {PERSON}{TENSE}{VOICE}{MOOD_F}-{NUMBER}--",
    f"V- -{TENSE_1}{VOICE}N----",
    f"V- -{TENSE_1}{VOICE}P{CNG_V}-",
]
