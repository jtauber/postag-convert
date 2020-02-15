PERSON = "[123]"
PERSON_ = "[-123]"
NUMBER = "[sdp]"
NUMBER_ = "[-sdp]"
VOICE = "[aemp]"
VOICE_ = "[-aemp]"
GENDER = "[fmn]"
GENDER_ = "[-fmn]"
CASE = "[navgd]"
CASE_ = "[-navgd]"
DEGREE_ = "[-cs]"

REGEXES1 = [
    "c--------",
    "d--------",
    "g--------",
    "i--------",
    "r--------",
    "u--------",

    "x-[-sp]---[-n][-nad]-",

    f"m-{NUMBER_}---{GENDER_}{CASE_}-",

    f"a-{NUMBER}---{GENDER_}{CASE_}{DEGREE_}",
    f"l-{NUMBER}---{GENDER}{CASE}-",
    f"n-{NUMBER_}---{GENDER_}{CASE_}-",
    f"p{PERSON_}{NUMBER_}---{GENDER_}{CASE_}-",

    f"v{PERSON}{NUMBER}[-pifarlt][miso]{VOICE}---",
    f"v--[-pafrt]n{VOICE}---",
    f"v-{NUMBER}[pafr]p{VOICE}{GENDER}{CASE}-",

    # @@@ ERRORS IN CELANO
    
    "v--amm---",  # @@@ imperative without person or number
    "v-samp---",  # @@@ imperative without person
    "v-spna---",  # @@@ infinitive with number
    "v3s------",  # @@@ person-number but nothing else
    "v3said---",  # @@@ what is voice=d?
    "v--pnd---",  # @@@ what is voice=d?

    "v-[sp][ap]p-mn-",  # @@@ participle missing voice
    "v-sapa-a-",  # @@@ participle missing gender
    "v--[ar]n----",  # @@@ infinitive missing voice
    "v3-roe---",  # @@@ finite verb missing number
    "v[123][sp][ifa][io]----",  # @@@ finite verb missing voice
]

REGEXES2 = [
    "----------",

    "c---------",
    "g[-m]--------",
    "i---------",
    "r---------",

    f"d[-deirx]-------{DEGREE_}",

    f"a[-ev]-{NUMBER}---{GENDER_}{CASE}{DEGREE_}",
    f"m--[-sp]---{GENDER_}[-nagd]-",
    f"n[-e]-{NUMBER_}---{GENDER_}{CASE}-",
    f"p[-acdikprsx]-{NUMBER}---{GENDER_}{CASE}-",

    f"v[-c]{PERSON}{NUMBER}[pifarlt][miso]{VOICE}---",
    f"v[-c]--[pafrt]n{VOICE}---",
    f"v[-c]-{NUMBER}[pafr]p{VOICE}{GENDER}{CASE}-",
]
