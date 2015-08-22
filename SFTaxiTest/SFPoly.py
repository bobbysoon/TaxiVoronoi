from sfml import sf

#from SFCircle import *
from SFBorder import *

from SFLineStrip import *
from SFTriFan import *

from time import time

class SFPoly(sf.Drawable):
	def __init__(self, poly,verts):
		self.poly= poly
		self.verts= [verts[vi] for vi in poly.verts]
		sf.Drawable.__init__(self)
		self.blackBorder=	SFLineStrip(self.verts,col=sf.Color(128,128,128))
		self.triFan=	SFTriFan([poly.centroid]+self.verts,col=sf.Color.WHITE)
		self.sfBorders= [SFBorder(b,verts) for b in poly.borders]

	def setScale(self,scale):
		return
		for b in self.sfBorders:
			b.setScale(scale)
	def updateRays(self, corners):
		return
		for b in self.sfBorders: b.updateRays(corners)

	def draw(self, target,states,selected=False):
		if selected:
			l=len(self.verts)
			for i in range(l):
				c= (256.0*i/l+time()*250.0) % 256
				self.triFan[1+i].color = sf.Color(c,0,255-c)
				target.draw(self.triFan , states)
		else:
			target.draw( self.blackBorder , states)

