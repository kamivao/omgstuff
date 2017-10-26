from __future__ import print_function, unicode_literals, division

import re
import itertools
import nltk
from nltk.tag import hmm

from six.moves import map, zip

try:
    import numpy as np
except ImportError:
    pass

from nltk.probability import (FreqDist, ConditionalFreqDist,
                              ConditionalProbDist, DictionaryProbDist,
                              DictionaryConditionalProbDist,
                              LidstoneProbDist, MutableProbDist,
                              MLEProbDist, RandomProbDist)
from nltk.metrics import accuracy
from nltk.util import LazyMap, unique_list
from nltk.compat import python_2_unicode_compatible
from nltk.tag.api import TaggerI
#from nltk.tag.hmm import HiddenMarkovModelTrainer
#from nltk.tag.hmm import HiddenMarkovModelTagger
#from nltk.tag.hmm import load_pos
from nltk.tag.hmm import *


from nltk.corpus import brown

def demo_pos():
    # demonstrates POS tagging using supervised training

    print()
    print("HMM POS tagging demo")
    print()

    print('Training HMM...')
    labelled_sequences, tag_set, symbols = load_pos(20000)
    trainer = HiddenMarkovModelTrainer(tag_set, symbols)
    hmm = trainer.train_supervised(labelled_sequences[10:],
                    estimator=lambda fd, bins: LidstoneProbDist(fd, 0.1, bins))

    print('Testing...')
    hmm.test(labelled_sequences[:10], verbose=True)
    print(hmm.tag("Today is a good day .".split()))
    print(hmm.best_path("Today is a good day .".split()))

demo_pos()

