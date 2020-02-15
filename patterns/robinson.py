CASE_V = "[NAVGD]"
CASE = "[NAGD]"
GENDER = "[FMN]"
PERSON = "[123]"
NUMBER = "[SP]"

CNG = f"{CASE}{NUMBER}{GENDER}"
CNG_V = f"{CASE_V}{NUMBER}{GENDER}"

REGEXES = [
    "ADV(-[CIKNS])?",
    "COND(-K)?",  # ἐάν.1437 εἰ.1487 εἴγε.1489 εἴ.1512 εἴ.1513 (-K) κἄν.2579
    "CONJ(-N)?",
    "HEB",
    "PREP",
    "PRT(-[IN])?",
    "N-PRI",
    "A-NUI(-ABB)?",
    "N-LI",  # Ω.5598 Α.1 ἰῶτα.2503
    "INJ",  # οὐαί.3759 ὦ.5599 οὐά.3758 ἔα.1436
    "N-OI",  # ὄναρ.3677 οὐαί.3759 σίκερα.4608
    "ARAM",

    f"A-{CNG_V}(-[CNS]|-ATT)?",
    f"C-[AGD][P][MN]",  # ἀλλήλων.240
    f"D-{CNG}(-K)?",  # ὅδε.3592 οὗτος.3778 ἐκεῖνος.1565 τοιόσδε.5107 τοιοῦτος.5108 τοσοῦτος.5118 τηλικοῦτος.5082 (-K) κἀκεῖνος.2548
    f"F-[123][AGD]{NUMBER}{GENDER}",  # αὑτοῦ.848 ἑαυτοῦ.1438 ἐμαυτοῦ.1683 σεαυτοῦ.4572
    f"I-{CNG}",  # τίς.5101 ποῖος.4169
    f"K-{CNG}",  # οἷος.3634 ὅσος.3745
    f"N-{CNG_V}(-[CS])?",
    f"P-[12]{CASE}{NUMBER}(-K)?",  # σύ.4771 ἐγώ.1473 ἡμεῖς.2249 ὑμεῖς.5210 (-K) κἀγώ.2504
    f"P-{CNG}",  # αὐτός.846
    f"Q-{CNG}",  # πόσος.4214
    f"R-{CNG}(-ATT)?",  # ὅς.3739 οἷος.3634 ὅστις.3748
    f"S-[12][SP]{CNG}",  # σός.4674 ἐμός.1699 ἡμέτερος.2251 ὑμέτερος.5212
    f"T-{CNG}",  # ὁ.3588
    f"X-{CNG}",  # τὶς.5100 δεῖνα.1170

    f"V-[PIFARL][ADEMNOP][IMOS]-{PERSON}{NUMBER}(-ATT)?",
    f"V-2[FARL][ADMNOP][IMOS]-{PERSON}{NUMBER}(-ATT)?",
    "V-[PFAR][ADEMNOP]N(-ATT)?",
    "V-2[AR][ADMOP][N]",
    f"V-[PFAR][ADEMNOP]P-{CNG_V}(-ATT)?",
    f"V-2[AR][ADMP]P-{CNG}(-ATT)?",

    f"V-RPR-ASN",  # @@@ ERROR?
]
