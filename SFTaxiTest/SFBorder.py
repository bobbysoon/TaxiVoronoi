from sfml import sf
from SFCircle import *

from TaxiVoronoi.Intersect import RaySegIntersect
from TaxiVoronoi.SegRay import *

def ScreenEdgeIntersect(corners,rayOrigin,rayDirection):
	edges= [ Seg(corners[i-1],corners[i]) for i in [0,1,2,3] ]
	rayIntersects = [RaySegIntersect( Ray(rayOrigin,rayOrigin+rayDirection), edge) for edge in edges]
	rayIntersects = [p for p in rayIntersects if p]
	return rayIntersects[0] if rayIntersects else None

class _SFBorder(sf.VertexArray):
	def __init__(self, border):
		self.border= border
		sf.VertexArray.__init__(self, sf.PrimitiveType.LINES_STRIP,4 )
		self[1].position= border.lines[1][0]
		self[2].position= border.lines[1][1]
		for i in [0,1,2,3]: self[i].color= sf.Color.BLACK
		self.vertCircle= SFCircle( oc=sf.Color.RED , ic=sf.Color.TRANSPARENT )
	def updateRays(self, corners):
		p0= ScreenEdgeIntersect(corners, self[1].position,-self.border.axis)
		p3= ScreenEdgeIntersect(corners, self[2].position, self.border.axis)
		if p0: self[0].position= p0
		if p3: self[3].position= p3
	def setScale(self,scale):
		self.vertCircle.setScale(scale)
	def draw(self, target,states):
		target.draw(self,states)
		for p in self.border.verts:
			self.vertCircle.draw(target,states,p)

class SFBorder(sf.VertexArray):
	def __init__(self, border, verts):
		self.border= border
		sf.VertexArray.__init__(self, sf.PrimitiveType.LINES_STRIP, len(border.verts) )
		c=0.0;cs=255.0/(len(border.verts)-1)
		for i in range(len(border.verts)):
			self[i].position= verts[border.verts[i]]
			self[i].color= sf.Color(c,c,c)
			c+= cs
	def draw(self, target,states):
		target.draw(self,states)

