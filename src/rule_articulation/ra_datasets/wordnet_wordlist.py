import random
from functools import cache
from itertools import islice
from typing import Iterator

import nltk

from nltk.corpus import wordnet

from rule_articulation.task_model import LabelledInput, RuleDataset


def is_palindrome(word: str) -> bool:
    """Ignores case and non-alphanumeric characters."""
    lower_cased_word = [c for c in word.lower() if c.isalpha() or c.isnumeric()]
    return lower_cased_word == lower_cased_word[::-1]


class PalindromeWordDataset(RuleDataset):
    all_words: list[str]

    # Constructed by getting the palindromes from the wordnet list
    # and adding anything from https://en.wiktionary.org/wiki/Appendix:English_palindromes
    palindromes: list[str] = [
        "aa",
        "aaa",
        "aba",
        "abba",
        "acca",
        "ada",
        "adda",
        "adinida",
        "aeaea",
        "affa",
        "aga",
        "aha",
        "aiaia",
        "aibohphobia",
        "akasaka",
        "akka",
        "ala",
        "alala",
        "alla",
        "alula",
        "ama",
        "amma",
        "ana",
        "anna",
        "anona",
        "aoxomoxoa",
        "ara",
        "arara",
        "ardra",
        "atta",
        "ava",
        "aviva",
        "awa",
        "Beeb",
        "bib",
        "bob",
        "Bob",
        "boob",
        "brb",
        "bub",
        "Capac",
        "cbc",
        "ccc",
        "cdc",
        "cfc",
        "civic",
        "ctc",
        "dad",
        "debed",
        "ded",
        "deed",
        "degged",
        "deified",
        "deked",
        "deled",
        "deleveled",
        "denned",
        "dered",
        "detartrated",
        "dewed",
        "dexed",
        "did",
        "dmd",
        "dod",
        "dud",
        "dvd",
        "ee",
        "egarage",
        "eke",
        "ele’ele",
        "eleele",
        "elle",
        "eme",
        "ene",
        "ere",
        "ese",
        "esse",
        "eve",
        "evitative",
        "ewe",
        "eye",
        "gag",
        "gig",
        "glenelg",
        "gog",
        "goog",
        "hadedah",
        "hagigah",
        "hah",
        "halalah",
        "hallah",
        "hamah",
        "hamamah",
        "Hannah",
        "hararah",
        "heh",
        "huh",
        "igigi",
        "Igigi",
        "iii",
        "immi",
        "irori",
        "isi",
        "kaiak",
        "kanak",
        "kayak",
        "kazak",
        "keek",
        "kelek",
        "kinnikinnik",
        "kkk",
        "kodok",
        "kook",
        "krk",
        "laval",
        "ldl",
        "level",
        "liril",
        "lol",
        "ma'am",
        "madam",
        "malayalam",
        "mallam",
        "mam",
        "markram",
        "marram",
        "mem",
        "mim",
        "minim",
        "mm",
        "mom",
        "mum",
        "murdrum",
        "mym",
        "naan",
        "nan",
        "nan",
        "natan",
        "nauruan",
        "nauruan",
        "navan",
        "nen",
        "neven",
        "non",
        "noon",
        "Noyon",
        "nun",
        "odo",
        "ofo",
        "ogopogo",
        "oho",
        "omo",
        "ono",
        "oo",
        "oppo",
        "oruro",
        "oto",
        "otto",
        "Otto",
        "oxo",
        "OXO",
        "pap",
        "pcp",
        "peep",
        "peeweep",
        "pep",
        "pip",
        "pip-pip",
        "poop",
        "pop",
        "ppp",
        "pull-up",
        "pup",
        "put-up",
        "qaanaaq",
        "racecar",
        "radar",
        "redder",
        "redivider",
        "refer",
        "reifier",
        "releveler",
        "renner",
        "repaper",
        "reviver",
        "revver",
        "rotator",
        "rotavator",
        "rotor",
        "sagas",
        "salas",
        "sas",
        "sees",
        "seities",
        "seles",
        "selles",
        "sememes",
        "semes",
        "senones",
        "seres",
        "Serres",
        "sesses",
        "sexes",
        "shahs",
        "sinis",
        "siris",
        "sis",
        "sixaxis",
        "sls",
        "solos",
        "soosoos",
        "sos",
        "sss",
        "stats",
        "stets",
        "stots",
        "succus",
        "sulus",
        "sus",
        "qusus",
        "tacocat",
        "tat",
        "tattarrattat",
        "tdt",
        "tebet",
        "tenet",
        "terret",
        "tet",
        "tevet",
        "tibit",
        "tirrit",
        "tit",
        "tnt",
        "toot",
        "torot",
        "tot",
        "tumut",
        "tut",
        "tut-tut",
        "utu",
        "vav",
        "wakaw",
        "waw",
        "wnw",
        "wow",
        "wsw",
        "www",
        "xanax",
        "xenex",
        "xix",
        "xxx",
        "yay",
        "zerorez",
        "zuz",
        "zzz",
    ]

    def __init__(self):
        nltk.download("wordnet")
        all_words = list(wordnet.words())
        random.shuffle(all_words)
        self.all_words = all_words

    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        num_of_palindromes = sum(labels)
        non_palindromes_iter = iter(
            self.get_non_palindromes(len(labels) - num_of_palindromes)
        )
        palindromes_iter = iter(random.sample(self.palindromes, k=num_of_palindromes))

        return [
            LabelledInput(
                input=next(palindromes_iter) if label else next(non_palindromes_iter),
                label=label,
            )
            for label in labels
        ]

    def get_non_palindromes(self, n: int) -> Iterator[str]:
        """Make sure we return n different words, and no palindromes."""
        returned_words: set[str] = set()
        while len(returned_words) < n:
            candidate = random.choice(self.all_words)
            if len(candidate) == 1:
                continue

            if candidate in returned_words:
                continue

            if is_palindrome(candidate):
                continue

            if "_" in candidate:
                # the non-palindrome dataset contains "words" that are actually several words (e.g. "camphor_oil" and "plant_scientist")
                continue

            # otherwise, accept
            returned_words.add(candidate)
            yield candidate
