# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2014-12-15 20:24
# modified : 2014-12-15 20:24
"""
Example for timing ipa2tokens vs. tokenizer functions using orthoprofiles in
LingPy.
"""

__author__="Johann-Mattis List"
__date__="2014-12-15"


import timeit


stm1 = 'f1 = lambda x: [ipa2tokens(y) for y in x]'
stm2 = 't=Tokenizer();f2 = lambda x: [t.combine_modifiers(t.tokenize(s)) for s in x]'

stm3 = "[x[0] for x in csv2list(test_data('test_tokenization.csv'))]"

t1 = timeit.timeit(stm1+';'+'f1('+stm3+')', setup="from lingpy.tests.util import test_data;from lingpy import csv2list,ipa2tokens", number=10)
t2 = timeit.timeit(stm2+';'+'f2('+stm3+')', setup="from lingpy.tests.util import test_data; from lingpy import csv2list; from lingpy.sequence.tokenizer import Tokenizer", number=10)

print(t1)
print(t2)
