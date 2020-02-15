CASE = "[NAVGDC]"
GENDER = "[FMNXYZ]"
PERSON = "[123]"
NUMBER = "[SP]"
VOICE = "[AMP]"
TENSE = "[PIFAXY]"
TENSE_1 = "[PFAX]"
MOOD_F = "[DISO]"

CN_ = f"{CASE}{NUMBER}-"
CNG = f"{CASE}{NUMBER}{GENDER}"

REGEXES = [
    "-------",
    f"----{CN_}",
    f"----{CNG}",
    f"{TENSE}{VOICE}{MOOD_F}{PERSON}-{NUMBER}-",
    f"{TENSE_1}{VOICE}N----",
    f"{TENSE_1}{VOICE}P-{CNG}",
]
