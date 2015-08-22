#!/usr/bin/python

from time import time
from RandomPointGrid import *
from TaxiVoronoi import TaxiVoronoi
from random import seed
from SFTaxiTest import SFTaxiTest

seed(2)

startTime=time()
polies,verts= TaxiVoronoi(RandomPointGrid( gridSize=4 , noise=2.5 ))
print 'TIME:%.2f'%(time()-startTime)

SFTaxiTest(polies,verts)
