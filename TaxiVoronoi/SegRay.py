from Intersect import *
from Vec2 import *

class Ray(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Ray, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersection(self,other):
		if other.__class__ is Seg:	return RaySegIntersect(self,other)
		if other.__class__ is Ray:	return RayRayIntersect(self,other)

class Seg(tuple):
	def __new__(self, r1,r2=None):
		if type(r2) is None: r1,r2=r1
		r1x,r1y=r1;r2x,r2y=r2
		return tuple.__new__(Seg, (Vec2(r1x,r1y),Vec2(r2x,r2y)) )

	def intersection(self,other):
		if other.__class__ is Seg:	return SegSegIntersect(other,self)
		if other.__class__ is Ray:	return RaySegIntersect(other,self)

