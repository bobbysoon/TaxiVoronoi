from random import random as rnd

from TaxiVoronoi import Vec2

def RandomPointGrid(noise=1.0,gridSize=8,scale=(1.0,1.0)):
	P=[]
	wd,ht=scale
	psx,psy= Vec2(float(wd),float(ht))/float(gridSize)
	for i in range(gridSize):
		y=(0.5+i)*psy
		for j in range(gridSize):
			x=(0.5+j)*psx
			P.append( Vec2(psx*(rnd()-rnd())*noise/2.0+x,psy*(rnd()-rnd())*noise/2.0+y) )
	return P
