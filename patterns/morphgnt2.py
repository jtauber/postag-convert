CASE = r"(?P<case>[NAVGDC])"
GENDER = r"(?P<gender>[FMNXYZ])"
PERSON = r"(?P<person>[123])"
NUMBER = r"(?P<number>[SP])"
VOICE = r"(?P<voice>[AMP])"
TENSE = r"(?P<tense>[PIFAXY])"
TENSE_1 = r"(?P<tense>[PFAX])"
MOOD_F = r"(?P<mood>[DISO])"
MOOD_N = r"(?P<mood>N)"
MOOD_P = r"(?P<mood>P)"

CN_ = f"{CASE}{NUMBER}-"
CNG = f"{CASE}{NUMBER}{GENDER}"

REGEXES = [
    "-------",
    f"----{CN_}",
    f"----{CNG}",
    f"{TENSE}{VOICE}{MOOD_F}{PERSON}-{NUMBER}-",
    f"{TENSE_1}{VOICE}{MOOD_N}----",
    f"{TENSE_1}{VOICE}{MOOD_P}-{CNG}",
]
