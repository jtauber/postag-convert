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
    "c--------",  # conjunction
    "d--------",  # adverb
    "g--------",  # particle
    "i--------",  # interjection
    "r--------",  # preposition
    "u--------",  # punctuation

    "x-[-sp]---[-n][-nad]-",  # @@@

    f"m-{NUMBER_}---{GENDER_}{CASE_}-",  # numeral

    f"a-{NUMBER}---{GENDER_}{CASE_}{DEGREE_}",  # adjective
    f"l-{NUMBER}---{GENDER}{CASE}-",  # article
    f"n-{NUMBER_}---{GENDER_}{CASE_}-",  # noun
    f"p{PERSON_}{NUMBER_}---{GENDER_}{CASE_}-",  # pronoun

    f"v{PERSON}{NUMBER}[-pifarlt][miso]{VOICE}---",  # finite verb
    f"v--[-pfart]n{VOICE}---",  # infinitive
    f"v-{NUMBER}[pafr]p{VOICE}{GENDER}{CASE}-",  # participle

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

    "c---------",  # conjunction
    "g[-m]--------",  # particle (gm = modal particle, e.g. κε)
    "i---------",  # interjection, e.g. ὀτοτοί
    "r---------",  # prerposition

    # e- exclamation
    # y- math term (Euclid's ΑΒΓ geometrical figures)

    # adverb
    # dd = demonstrative adverb, e.g. ταύτῃ
    # de = proper name adverb, e.g. Ἀθήναζε
    # di = interrogative adverb, e.g. ποῦ
    # dr = reltive adverb, e.g. οἷ
    # dx = indefinite adverb, e.g. που
    f"d[-deirx]-------{DEGREE_}",

    f"a[-ev]-{NUMBER}---{GENDER_}{CASE}{DEGREE_}",  # adjective (ae = proper adjective; av = @@@)
    f"m--[-sp]---{GENDER_}[-nagd]-",  # numeral
    f"n[-e]-{NUMBER_}---{GENDER_}{CASE}-",  # noun (ne = proper noun)

    # no x-
    # no l- (see pa below)

    # pronoun
    # pa = definite article (not l-)
    # pc = reciprocal pronoun, e.g. ἀλλήλους
    # pd = demonstrative pronoun, e.g. οὗτος
    # pi = interrogative pronoun, e.g. τίς
    # pk = reflexive pronoun, e.g. σεαυτόν
    # pp = personal pronoun, e.g. με
    # pr = relative pronoun, e.g. ὅς
    # ps = possessive pronoun, e.g. ἐμός
    # px = indefinite pronoun, e.g. τις
    f"p[-acdikprsx]-{NUMBER}---{GENDER_}{CASE}-",

    f"v[-c]{PERSON}{NUMBER}[pifarlt][miso]{VOICE}---",  # finite verb
    f"v[-c]--[pafrt]n{VOICE}---",  # infinitive
    f"v[-c]-{NUMBER}[pafr]p{VOICE}{GENDER}{CASE}-",  # participle
]

REGEXES3 = [
    # @@@ what do underscores mean?

    "_--------",  # @@@
    "c-------[-_]",  # conjunction
    "d-------[-_pcs]",  # adverb (why degree=p?)
    "d-p---ma-",  # @@@
    "e--------",  # exclamation
    # @@@ no g ?
    "i--------",  # interjection
    "r-------[-_]",  # preposition
    "r-s---fv-",  # @@@
    "u--------",  # punctuation

    "x-[-sp]---[-mn][-na]-",  # @@@

    "m-[-_p]---[-_m][-_]-",  # numeral

    "a-[-_sdp]---[-_fmn][-_navgd][-_pcs]",  # adjective
    "l-[-sdp]---[-fmn][-navgd]-",  # article
    "n-[-_sdp]---[-_fmn][_navgd][-_]",  # noun
    "p[-123][_sdp]---[-_fmn][_navgd]-",  # pronoun

    f"v{PERSON}{NUMBER}[-pifarlt][-miso]{VOICE}---",  # finite verb
    f"v[-_][-_][pfart]n{VOICE}---",  # infinitive
    f"v-{NUMBER}[pafr]p{VOICE}{GENDER}{CASE}[-_]",  # participle

    "t-[sp][ap]p[ae]m[nd]-",  # @@@ what is this?
    "v_____---",  # @@@

    "v-p-pmma-",  # @@@ ERROR
    "v--ppamg-",  # @@@ ERROR

    "v--[p][i][a]---",  # @@@ ERROR

    ".........-----",  # @@@ ERROR

    "c2sfim---",  # @@@ ERROR

    "n-s---fl-",  # @@@ what is case=l ?
    "v--ina---",  # @@@ can't have imperfect infinitive
    "v--pnd---",  # @@@ can't have voice=d
    "v.[sp].n.---",  # @@@ can't have number if infinitive
    "v.......[pc]",  # @@@ can't have verb with degree
    "v-..g....",  # @@@ can't have mood=g
    "v-ppmang-",  # @@@ can't have mood=m with case, etc
    "v-s[ap]i[ae]mn-",  # @@@
    "v-slpemn_",  # @@@
    "v1[sp]fimf--",  # @@@
    "v3..p....",  # @@@ participle with person
    "v-..p-...",  # @@@ participle without a voice
    "v3s------",  # @@@
    "v3said---",  # @@@
    "v3spi----",  # @@@
]
