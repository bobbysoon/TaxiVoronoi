from sfml import sf

from TaxiVoronoi.Math import *

from SFPoly import *
from SFCircle import *

def pointInPoly(p,poly):
	x,y=p

	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y
	return inside


class Text(sf.Text):
	def __init__(self):
		sf.Text.__init__(self,font=sf.Font.from_file("/usr/share/fonts/truetype/freefont/FreeMono.ttf"))

class SFObjects(sf.Drawable):
	def __init__(self, polies,verts):
		sf.Drawable.__init__(self)
		self.polies= polies
		self.verts= verts
		P= [poly.centroid for poly in polies]
		self.sfPolies= { tuple(P[i]):SFPoly(polies[i],verts) for i in range(len(polies)) }
		self.clickedAt= self.selectPoly
		self.selectedPoly=None
		self.vertCirc= SFCircle( oc=sf.Color.TRANSPARENT , ic=sf.Color(0,0,255,128) )
		self.pc=0
		self.text=Text()

	def setScale(self,scale):
		self.vertCirc.setScale(2.5*scale)
		self.text.ratio=scale,scale
		#if self.selectedPoly:
		#	self.selectedPoly.setScale(scale)

	def updateRays(self, corners):
		pass
		#for c in self.sfPolies: self.sfPolies[c].updateRays(corners)

	def draw(self, target,states):
		if self.selectedPoly:
			self.selectedPoly.draw(target, states, True)
		for c in self.sfPolies:
			sfPoly= self.sfPolies[c]
			if sfPoly!=self.selectedPoly:
				sfPoly.draw(target, states)

		pc= 0
		for p in self.verts:
			if pointInPoly(p,self.quadCorners): pc+=1
			self.vertCirc.draw(target,states,p)
		if pc != self.pc:
			self.text.string= ('%i vert%s'%(pc,'s' if pc!=1 else '')).rjust(10)
			self.pc=pc

		self.text.position= self.quadCorners[0]
		self.text.rotation= target.view.rotation
		target.draw(self.text)
		#self.text.draw(target,states)

	def selectPoly(self, p):
		dists = {mDist(p,c):self.sfPolies[c] for c in self.sfPolies}
		self.selectedPoly = dists[min(dists.keys())]


