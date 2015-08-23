#!/usr/bin/python

from RandomPointGrid import *
from TaxiVoronoi import TaxiVoronoi
from SFTaxiTest import SFTaxiTest

from random import seed,randint
from sys import maxint,argv
if argv[1:]: s=int(argv[1])
else:
	s = randint(0, maxint )
	print 'seed:\t%i'%s
seed(s)

polies,verts= TaxiVoronoi(RandomPointGrid( gridSize=8 , noise=2.5 ))

SFTaxiTest(polies,verts)
