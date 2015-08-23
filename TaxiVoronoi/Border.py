from Intersect import *

from Math import *

class Border:
	def __getitem__(self, key):
		return self.verts[key]
	def __setitem__(self, key,val):
		self.verts[key]=val
	def __len__(self):
		return len(self.verts)
	def reverse(self):
		self.verts.reverse()

	def __init__(self, c,oc ):
		self.centroids= [c,oc]

		dx,dy=oc-c
		ax,ay=abs(dx),abs(dy)
		sx,sy=sgn(dx),sgn(dy)

		self.isLine= abs(ax-ay)<G.epsilon or ax<G.epsilon or ay<G.epsilon
		if self.isLine:
			print dx,dy
		#else:
		diag = Vec2(-dx,sy*ax)/2.0 if ax<ay else Vec2(sx*ay,-dy)/2.0 if ax>ay else Vec2(-dx/2.0,dy/2.0)

		cp= (c+oc)/2.0
		p1,p2 = cp+diag,cp-diag
		self.axis= Vec2(sx,0.0) if ax<ay else Vec2(0.0,sy) if ax>ay else None

		self.seg= Seg(p1,p2)
		self.lines= [Ray(p1,p1-self.axis),self.seg,Ray(p2,p2+self.axis)]

	def intersect(self,other):
		pa=[]
		l1,l2 = self.lines,other.lines
		for li,lj in [(li,lj) for li in l1 for lj in l2]:
			p=li.intersection(lj)
			if p: pa.append( p )
		return pa

