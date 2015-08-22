from sfml import sf

class Quad(sf.VertexArray):
	def __init__(self):
		sf.VertexArray.__init__(self, sf.PrimitiveType.QUADS,4)
		for i in [0,1,2,3]: self[i].color=sf.Color.BLUE

	def align(self, target):
		sw,sh= target.size
		pa = [(0,0),(sw,0),(sw,sh),(0,sh)]
		for i in [0,1,2,3]:
			p=	target.map_pixel_to_coords(pa[i])
			self[i].position= p
			self[i].tex_coords= p

	def corners(self):
		return [self[i].position for i in [0,1,2,3]]
