#!/usr/bin/python


class G:
	clockwise=False
	ccw= not clockwise
	WindingOrderUsed = ccw
	epsilon = 1e-04

from sfml.sf import Vector2 as Vec2

class Ray(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Ray, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersect(self,other):
		if other.__class__ is Seg:	return RaySegIntersect(self,other)
		if other.__class__ is Ray:	return RayRayIntersect(self,other)
		if other.__class__ is Line:	return RayLineIntersect(self,other)

class Seg(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Seg, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersect(self,other):
		if other.__class__ is Seg:	return SegSegIntersect(other,self)
		if other.__class__ is Ray:	return RaySegIntersect(other,self)
		if other.__class__ is Line:	return SegLineIntersect(self,other)

class Line(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Line, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersect(self,other):
		if other.__class__ is Seg:	return SegLineIntersect(other,self)
		if other.__class__ is Ray:	return RayLineIntersect(other,self)
		if other.__class__ is Line:	return LineLineIntersect(other,self)

def TrisectPoint(p):
	cdef float minDist1,minDist2,minDist3,dx,dy,d
	minDist1,minDist2,minDist3=32767,32767,32767
	for c in G.P:
		dx,dy=c[0]-p[0],c[1]-p[1]
		d=abs(dx)+abs(dy)
		if d<minDist3:
			if d<minDist2:
				minDist3=minDist2
				if d<minDist1:
					minDist2=minDist1
					minDist1=d
				else:
					minDist2=d
			else:
				minDist3=d
	return minDist2-minDist1<G.epsilon and minDist3-minDist2<G.epsilon

def IntersectBorders(l1,l2):
	verts = []
	for li,lj in [(li,lj) for li in l1 for lj in l2]:
		p = li.intersect(lj)
		if p and TrisectPoint(p): verts.append( p )
	return verts

def _IntersectBorders(l1,l2):
	verts=[]

	r11,s12,r13 = l1
	r21,s22,r23 = l2

	p=RayRayIntersect(r11,r21)
	if p and TrisectPoint(p):		verts.append(p)
	p=RayRayIntersect(r11,r23)
	if p and TrisectPoint(p):		verts.append(p)
	p=RayRayIntersect(r13,r21)
	if p and TrisectPoint(p):		verts.append(p)
	p=RayRayIntersect(r13,r23)
	if p and TrisectPoint(p):		verts.append(p)

	p=RaySegIntersect(r11,s22)
	if p and TrisectPoint(p):		verts.append(p)
	p=RaySegIntersect(r13,s22)
	if p and TrisectPoint(p):		verts.append(p)
	p=RaySegIntersect(r21,s12)
	if p and TrisectPoint(p):		verts.append(p)
	p=RaySegIntersect(r23,s12)
	if p and TrisectPoint(p):		verts.append(p)

	p=SegSegIntersect(s12,s22)
	if p and TrisectPoint(p):		verts.append(p)

	return verts



def SegSegIntersect(s1,s2):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = s1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = s2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		s = ( dy13*dx21 - dx13*dy21) / d
		if r >= 0 and r <= 1 and s >= 0 and s <= 1:
			return x1 + r*dx21 , y1 + r*dy21

def RaySegIntersect(ray,seg):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = ray ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = seg ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		s = ( dy13*dx21 - dx13*dy21) / d
		if r >= 0:
			return x1 + r * dx21 , y1 + r * dy21

def RayRayIntersect(r1,r2):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = r1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = r2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		s = ( dy13*dx21 - dx13*dy21) / d
		if r >= 0 and s >= 0:
			return x1 + r*dx21 , y1 + r*dy21


def LineLineIntersect(r1,r2):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = r1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = r2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		return x1 + r*dx21 , y1 + r*dy21

def SegLineIntersect(s1,s2):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = s1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = s2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		if r >= 0 and r <= 1:
			return x1 + r*dx21 , y1 + r*dy21

def RayLineIntersect(s1,s2):
	cdef float x1,y1,x2,y2,x3,y3,x4,y4 , dx21,dy21,dx43,dy43 , d , dx13,dy13,r,s

	p1,p2 = s1 ; x1,y1 = p1;x2,y2 = p2
	p3,p4 = s2 ; x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		if r >= 0:
			return x1 + r*dx21 , y1 + r*dy21
