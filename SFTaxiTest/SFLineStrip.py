from sfml import sf

class SFLineStrip(sf.VertexArray):
	def __init__(self, verts, col=None):
		sf.VertexArray.__init__(self, sf.PrimitiveType.LINES_STRIP, len(verts) )
		for i in range(len(verts)):	self[i].position= verts[i]
		if col:
			if type(col) is list:
				for i in range(len(verts)):	self[i].color=col[i]
			else:
				for i in range(len(verts)):	self[i].color=col

