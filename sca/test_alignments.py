# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2014-12-05 14:22
# modified : 2014-12-05 14:22
"""
Test the Aligmnents class of LingPy by applying it to Japanese dialect data.
"""

__author__="Johann-Mattis List"
__date__="2014-12-05"


from lingpy import *
from sys import argv

# load alignments object

if len(argv) < 2:
    f = 'BAI'
else:
    f = argv[1]
alm = Alignments('tsv/'+f+'.tsv', ref="cogid")
alm.align(method='progressive')

alm.output('msa', style="normal")
alm.output('html')
alm.output('alm')
