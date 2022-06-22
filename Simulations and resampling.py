# -*- coding: utf-8 -*-
'''
Title
=====

Big Idea: Simulations and resampling using Python


Topics Covered
==============

* 

Created on Sat Jun 11 12:54:08 2022

@author: vmgon
'''

from random import *
from statistics import *
from collections import *

#%% Six roulette spins --  18 red, 18 black, 2 green

choice(['red', 'red', 'red', 'black', 'black', 'green'])

choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2)

population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
[choice(population) for i in range(6)]


Counter([choice(population) for i in range(6)])

# Even more elegant
choices(['red', 'black', 'green'], [18, 18, 2])

Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
# ^^^ This is the big idea with little code


#%% Deck of cards
deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, 20)

Counter(deal)



#%% Biased coin
pop = ['heads', 'tails']
wgt = [6, 4]
cumwgt = [.6, 1]

choices(pop, cumwgt, k = 7).count('heads')

trial = lambda : choices(pop, cumwgt, k = 7).count('heads') >= 5
n = 100000
sum(trial() for i in range(n)) / n


trial = lambda : choices(['heads', 'tails'], cum_weights = [0.6, 1.00], k = 7).count('heads') >= 5
n = 100000
sum(trial() for i in range(n)) / n