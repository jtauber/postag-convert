# Postag Schemes

## New MorphGNT proposals

* <https://github.com/morphgnt/sblgnt/wiki/Proposal-for-Gender-Tagging>
* <https://github.com/morphgnt/sblgnt/wiki/Proposal-for-Case-Tagging>
* <https://github.com/morphgnt/sblgnt/wiki/Handling-Ambiguity>


## CCAT/MorphGNT

See <https://github.com/morphgnt/sblgnt>.

### Part of Speech Code

`A-` adjective  
`C-` conjunction  
`D-` adverb  
`I-` interjection  
`N-` noun  
`P-` preposition  
`RA` definite article  
`RD` demonstrative pronoun  
`RI` interrogative/indefinite pronoun  
`RP` personal pronoun  
`RR` relative pronoun  
`V-` verb  
`X-` particle  

### Parsing Code

person (`1`=1st, `2`=2nd, `3`=3rd)  
tense (`P`=present, `I`=imperfect, `F`=future, `A`=aorist, `X`=perfect, `Y`=pluperfect)  
voice (`A`=active, `M`=middle, `P`=passive)  
mood (`I`=indicative, `D`=imperative, `S`=subjunctive, `O`=optative, `N`=infinitive, `P`=participle)  
case (`N`=nominative, `G`=genitive, `D`=dative, `A`=accusative)  
number (`S`=singular, `P`=plural)  
gender (`M`=masculine, `F`=feminine, `N`=neuter)  
degree (`C`=comparative, `S`=superlative)  

## Robinson

See <https://github.com/morphgnt/tischendorf/blob/master/docs/parscode.txt>.

### Uninflected Forms

`ADV` = ADVerb or adverb and particle combined  
`CONJ` = CONJunction or conjunctive particle  
`COND` = CONDitional particle or conjunction  
`PRT` = PaRTicle, disjunctive particle  
`PREP` = PREPosition  
`INJ` = INterJection  
`ARAM` = ARAMaic transliterated word (indeclinable)  
`HEB` = HEBrew transliterated word (indeclinable)  
`N-PRI` = Indeclinable PRoper Noun  
`A-NUI` = Indeclinable NUmeral (Adjective)  
`N-LI` = Indeclinable Letter (Noun)  
`N-OI` = Indeclinable Noun of Other type  

### Declined Forms

All follow the order: prefix-case-number-gender-(suffix)

Prefixes:

`N-` = Noun  
`A-` = Adjective  
`R-` = Relative pronoun  
`C-` = reCiprocal pronoun  
`D-` = Demonstrative pronoun  
`T-` = definite article  
`K-` = correlative pronoun  
`I-` = Interrogative pronoun  
`X-` = indefinite pronoun  
`Q-` = correlative or interrogative pronoun  
`F-` = reFlexive pronoun (person 1,2,3 added)  
`S-` = poSsessive pronoun (person 1,2,3 added)  
`P-` = Personal pronoun (person 1,2,3 added) > (Note: 1st and 2nd personal pronouns have no gender)  

Cases (5-case system only):

`-N` = Nominative
`-V` = Vocative
`-G` = Genitive
`-D` = Dative
`-A` = Accusative

Number:

`S` = Singular
`P` = Plural

Gender:

`M` = Masculine
`F` = Feminine
`N` = Neuter

Suffixes:

`-S` = Superlative (used only with adjectives and some adverbs)  
`-C` = Comparative (used only with adjectives and some adverbs)  
`-ABB` = ABBreviated form (used only with various numerals)  
`-I` = Interrogative  
`-N` = Negative (used only with particles as PRT-N)  
`-C` = Contracted form, or two words merged by crasis  
`-ATT` = ATTic Greek form  
`-P` = Particle attached (with relative pronoun)  

### Verbs

All Greek verbs are listed in one of three various forms:

1. V-tense-voice-mood
2. V-tense-voice-mood-person-number
3. V-tense-voice-mood-case-number-gender

The abbreviations which pertain to each of these categories are the following:

Tense:

`P` = Present  
`I` = Imperfect  
`F` = Future  
Second Future = `2F`  
`A` = Aorist  
Second Aorist = `2A`  
`R` = peRfect  
Second peRfect = `2R`  
`L` = pLuperfect  
Second pLuperfect = `2L`  
`X` = no tense stated (adverbial imperative)  

Voice:

`A` = Active  
`M` = Middle  
`P` = Passive  
`E` = Either middle or passive  
`D` = middle Deponent  
`O` = passive depOnent  
`N` = middle or passive depoNent  
`Q` = impersonal active  
`X` = no voice stated  

Mood:

`I` = Indicative  
`S` = Subjunctive  
`O` = Optative  
`M` = iMperative  
`N` = iNfinitive  
`P` = Participle  
`R` = impeRative-sense participle  

Extra:

`-M` = Middle significance  
`-C` = Contracted form  
`-T` = Transitive  
`-A` = Aeolic  
`-ATT` = Attic  
`-AP` = Apocopated form  
`-IRR` = Irregular or Impure form  

Person: `1`, `2`, `3` = First, Second, Third person

Number: `S`, `P` = Singular, Plural

Gender: `M`, `F`, `N` = Masculine, Feminine, Neuter

Case:

`N` = Nominative (5-case system only!)  
`G` = Genitive  
`D` = Dative  
`A` = Accusative  
`V` = Vocative  

## Morpheus

(from <https://github.com/gcelano/LemmatizedAncientGreekXML>)

1: part of speech

`n`: noun  
`v`: verb  
`a`: adjective  
`d`: adverb  
`l`: article  
`g`: particle  
`c`: conjunction  
`r`: preposition  
`p`: pronoun  
`m`: numeral  
`i`: interjection  
`u`: punctuation  

2: person

`1`: first person  
`2`: second person  
`3`: third person  

3: number

`s`: singular  
`p`: plural  
`d`: dual  

4: tense

`p`: present  
`i`: imperfect  
`r`: perfect  
`l`: pluperfect  
`t`: future perfect  
`f`: future  
`a`: aorist  

5: mood

`i`: indicative  
`s`: subjunctive  
`o`: optative  
`n`: infinitive  
`m`: imperative  
`p`: participle  

6: voice

`a`: active  
`p`: passive  
`m`: middle  
`e`: medio-passive  

7: gender

`m`: masculine  
`f`: feminine  
`n`: neuter  

8: case

`n`: nominative  
`g`: genitive  
`d`: dative  
`a`: accusative  
`v`: vocative  
`l`: locative  

9: degree

`c`: comparative  
`s`: superlative  

PhiloLogic extensions to part of speech:

`ae`: proper adjective (e.g., Ἀθηναῖος).  
`ne`: proper noun (eg., Ζεύς)  
`d-`: adverb" (eg., οὐ)  
`dd`: demonstrative adverb (eg., ταύτῃ)  
`de`: proper name adverb (eg., Ἀθήναζε)  
`di`: interrogative adverb (eg., ποῦ)  
`dr`: relative adverb (eg., οἷ)  
`dx`: indefinite adverb (eg., που)  
`c-`: conjunction (eg., καί)  
`r-`: preposition  
`p-`: pronoun  
`pa`: definite article  
`pc`: reciprocal pronoun (eg., ἀλλήλους)  
`pd`: demonstrative pronoun (eg., οὗτος)  
`pi`: interrogative pronoun (eg., τίς)  
`pk`: reflexive pronoun (eg., σεαυτόν)  
`pp`: personal pronoun (eg., με)  
`pr`: relative pronoun (eg., ὅς)  
`ps`: possessive pronoun (eg., ἐμός)  
`px`: indefinite pronoun (eg., τις)  
`m-`: numeral  
`i-`: interjection (eg., ὀτοτοί)  
`e-`: exclamation  
`y-`: math term or abbrev for all of Euclid's ΑΒΓ   geometrical figures  
`g-`: particle  
`gm`: modal particle (eg., κε)  
