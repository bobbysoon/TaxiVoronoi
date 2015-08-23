from Poly import *
from time import time

def Combinations(l):
	return [ (l[i],l[j]) for i in range(1,len(l)) for j in range(i) ]

def indexVert(v,verts):
	l= len(verts)
	for vi in range(l):
		dx,dy = verts[vi][0]-v[0],verts[vi][1]-v[1]
		d=max([abs(dx),abs(dy)])
		if d<G.epsilon:
			return vi
	verts.append(v)
	return l

def TaxiVoronoi(P):
	G.P= P
	polies= { tuple(c):Poly(c) for c in P }

	t=time()
	for poly in polies.values():
		poly.intersectBorders()
	print '%.3f'%(time()-t)

	for poly in polies.values():
		poly.sortBorderVerts()
		poly.indexVerts()
		poly.sequenceBorders()
		poly.sequenceVerts()

		poly.isClosed = poly.borders[0][0] == poly.borders[-1][-1]
		poly.correctWindingOrder()

	for centroid in polies:
		poly=polies[centroid]
		ca= [tuple(c) for b in poly.borders for c in b.centroids if c!=centroid]
		poly.neighborIndices = [P.index(c) for c in ca]
		poly.neighbors= [polies[c] for c in ca ]

	polies= [polies[tuple(p)] for p in P]
	verts=[]
	for p in polies:
		p.verts= [ indexVert(v,verts) for v in p.verts ]
		for b in p.borders:
			b.verts= [ p.verts[vi] for vi in b.verts ]

	return polies,verts

