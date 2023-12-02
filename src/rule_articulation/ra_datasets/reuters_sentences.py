from functools import cache

import nltk

from nltk.corpus import reuters


@cache
def get_reuters_sentences() -> list[str]:
    """Get Reuters sentences, excluding headlines and short/long sentences.
    32k sentences"""

    nltk.download("reuters")

    def is_headline(sentence):
        return sentence[:7].isupper()

    return [
        sentence.replace("\n", "")
        for sentence in nltk.sent_tokenize(reuters.raw())
        if not is_headline(sentence) and 40 < len(sentence) < 180
        # 75% of sentences are shorter than 180 characters, and 75% is longer than 83 characters; pd.DataFrame([len(sentence) for sentence in sentences_raw]).describe()
    ]