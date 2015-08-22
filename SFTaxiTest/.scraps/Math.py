from math import sqrt

def sgn(n): return 1.0 if n>0.0 else -1.0 if n<0.0 else 0.0

def dist(p1,p2):
	dx,dy=p1-p2
	return sqrt(dx*dx+dy*dy)

def mDist(p1,p2):
	dx,dy=p1-p2
	return abs(dx)+abs(dy)

