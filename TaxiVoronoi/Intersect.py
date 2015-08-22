#!/usr/bin/python

def SegSegIntersect(s1,s2):
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

def _RayRayIntersect(r1,r2):
	x1,y1= r1[0]
	x2,y2= r2[0]
	dx1,dy1= r1[1][0]-r1[0][0] , r1[1][1]-r1[0][1]
	dx2,dy2= r2[1][0]-r2[0][0] , r2[1][1]-r2[0][1]

	if not (dx1==dx2 or dy1==dy2):
		if dx1 and dx1*(x2-x1)>0: return x2,y1
		if dy1 and dy1*(y2-y1)>0: return x1,y2

def RayRayIntersect(r1,r2):
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


if __name__ == '__main__':
	e1=(1.,2.),(1.,4.)
	e2=(0.,1.),(4.,1.)
	print RayRayIntersect(e1,e2)