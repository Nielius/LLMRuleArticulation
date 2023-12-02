import nltk

from nltk.corpus import webtext, gutenberg, brown, reuters


from nltk.tokenize.treebank import TreebankWordDetokenizer
example = ['Here', 'I', 'have', 'a', 'sentence', ',', 'do', "n't", 'I', '?']
TreebankWordDetokenizer().detokenize(example)

# Alternative: bookcorpus
# https://huggingface.co/datasets/bookcorpus

nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('brown')

nltk.download('reuters')

sentences = list(reuters.sents())

import random

def stitch_sentence(words):
    return TreebankWordDetokenizer().detokenize(words)

some_sentences = random.sample(sentences, 10)

[ stitch_sentence(sentence) for sentence in some_sentences ]

import nltk

reuters.raw()

def is_headline(sentence):
    return sentence[:7].isupper()

sentences_raw = [
    sentence.replace("\n", "")
    for sentence in nltk.sent_tokenize(reuters.raw())
    if not is_headline(sentence)
    and len(sentence) < 180  # 75% of sentences are shorter than 180 characters; pd.DataFrame([len(sentence) for sentence in sentences_raw]).describe()
]

import pandas as pd

    
).to_csv("reuters_sentences.csv")


"AiDOIJ ASDIJ".isupper()

textsample ="This thing seemed to overpower and astonish the little dark-brown dog, and wounded him to the heart. He sank down in despair at the child's feet. When the blow was repeated, together with an admonition in childish sentences, he turned over upon his back, and held his paws in a peculiar manner. At the same time with his ears and his eyes he offered a small prayer to the child."

# !!! I should probably just use this sent_tokenize on the raw data?
sentences = nltk.sent_tokenize(textsample)

words = nltk.word_tokenize(textsample)
sentences
[w for w in words if w.isalpha()]


print(reuters.readme())

sentences = gutenberg.sents()

gutenberg.paras()


# >>> from nltk.tokenize.treebank import TreebankWordDetokenizer
# >>> example = ['Here', 'I', 'have', 'a', 'sentence', ',', 'do', "n't", 'I', '?']
# >>> TreebankWordDetokenizer().detokenize(example)
# "Here I have a sentence, don't I?"

from nltk.corpus import webtext
