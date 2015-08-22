from sfml import sf
from Quad import *
from Shader import *

class SFTaxiShader(sf.Drawable):
	def __init__(self, P):
		sf.Drawable.__init__(self)
		self.quad=		Quad()
		self.shader=	Shader(P)
		self.states=	sf.RenderStates(shader=self.shader)

	def draw(self, target,states):
		self.shader.set_parameter("iResolution", target.size )
		self.quad.align(target)
		target.draw(self.quad,self.states)

	def corners(self): return self.quad.corners()
