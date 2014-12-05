# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2014-12-05 15:40
# modified : 2014-12-05 15:40
"""
<++>
"""

__author__="Johann-Mattis List"
__date__="2014-12-05"

from lingpy import *


# we import lingpy proper and also lingpy.evaluate for comparing accuracy of
# alignments using lingpy
from lingpy import *
from lingpy.evaluate.apa import *

# get arguments to modify alignment
from sys import argv

from glob import glob

psas = glob('psa/*.psa')

for psa in psas:

    name = psa.split('/')[1]

    pair = PSA(psa)
    gold = PSA(psa)
    
    for mode in ['global', 'local', 'overlap', 'dialign']:

        for model in ['sca', 'dolgo', 'asjp']:

            pair.align(mode=mode, model=model)

            eva = EvalPSA(gold, pair)
            score = eva.c_score()

            print("{0:15} (with {1:7} mode and {2:5} sound class model) gets column-score {3}".format(
                name,
                mode,
                model,
                int(100 * score + 0.5)
                ))


