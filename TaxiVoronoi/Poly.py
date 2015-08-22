from Border import *

epsilon = 1e-04

clockwise=False
ccw= not clockwise
class Poly:
	WindingOrderUsed = ccw

	def __init__(self, c ):
		self.centroid= c
		self.borders= [ Border(c,oc) for oc in Poly.P if c!=oc ]

		for b in self.borders:
			b.verts= [p for p in list(b.seg) if self.RegionBorder(p)]

		self.intersectBorders()
		self.sortBorderVerts()
		self.indexVerts()
		self.sequenceBorders()
		self.sequenceVerts()

		self.isClosed = self.borders[0][0] == self.borders[-1][-1]
		self.correctWindingOrder()

	def RegionBorder(self, p):
		rDist= mDist(p,self.centroid)
		dists= sorted([ mDist(c,p) for c in Poly.P if c!=self.centroid ])
		return rDist-dists[0]<epsilon

	def TrisectPoint(self, p):
		dists= sorted([mDist(c,p) for c in Poly.P])
		return dists[1]-dists[0]<epsilon and dists[2]-dists[1]<epsilon

	def intersectBorders(self):
		B= self.borders
		for i,j in [(i,j) for i in range(1,len(B)) for j in range(i)]:
			pa= B[i].intersect(B[j])
			for p in pa:
				if self.TrisectPoint(p):
					B[i].verts.append(p)
					B[j].verts.append(p)
		self.borders= [b for b in self.borders if len(b)] # most don't intersect on this region's border

	def sortBorderVerts(self):
		for b in self.borders:
			if b.axis[0]:
				b.verts.sort(key=lambda x: x[0])
				#if b.axis[0]<0: b.verts.reverse()
			else:
				b.verts.sort(key=lambda x: x[1])
				#if b.axis[1]<0: b.verts.reverse()

	def indexVerts(self):
		self.verts=[]
		for b in self.borders:
			b.verts= [self.indexVert(v) for v in b.verts]

	def sequenceBorders(self):
		B= self.borders
		i,j=0,1
		while j<len(B):
			if		B[i][-1]==B[j][ 0]:							i,j=j,j+1
			elif	B[i][-1]==B[j][-1] or B[0][0]==B[j][0]:		B[j].reverse()
			elif	B[0][ 0]==B[j][-1]:							B.insert(0,B.pop(j))
			elif	j<len(B)-1:									B.append(B.pop(j))
			else:	assert False

	def sequenceVerts(self):
		B=self.borders
		V=self.verts
		assert not False in [B[bi-1][-1]==B[bi][0] for bi in range(1,len(B))]

		seq= B[0].verts + [vi for bi in range(1,len(B)) for vi in B[bi][1:]]
		for b in B:
			b.verts= [seq.index(vi) for vi in b.verts]
		self.verts= [V[vi] for vi in seq]

	def reverse(self):
		self.verts.reverse()
		self.borders.reverse()
		for b in self.borders: b.reverse()

	def correctWindingOrder(self):
		isClockwise = self.area_signed()>0
		if isClockwise != Poly.WindingOrderUsed: self.reverse()

	def indexVert(self, v):
		l= len(self.verts)
		for vi in range(l):
			dx,dy = self.verts[vi][0]-v[0],self.verts[vi][1]-v[1]
			d=max([abs(dx),abs(dy)])
			if d<epsilon:
				return vi
		self.verts.append(v)
		return l

	def area_signed(self):
		poly = self.verts[:-1] if self.isClosed else self.verts
		total,N = 0.0,len(poly)
		for i in range(N):
			v1,v2 = poly[i],poly[(i+1) % N]
			total += v1[0]*v2[1] - v1[1]*v2[0]
		return total/2

