from sfml import sf

class MouseCursor(sf.Drawable):
	def __init__(self, window):
		self.window= window
		sf.Drawable.__init__(self)
		self.vertArray= sf.VertexArray(sf.PrimitiveType.LINES,8)
		for i in range(4):
			self.vertArray[2*i].color= sf.Color.RED
			self.vertArray[2*i+1].color= sf.Color.TRANSPARENT

	def draw(self, target,states):
		self.pos= self.window.map_pixel_to_coords(sf.Mouse.get_position(self.window))
		mx,my= self.pos ; wd,ht= self.window.size ; sx,sy= self.window.view.size

		for i in range(4): self.vertArray[2*i].position= self.pos
		self.vertArray[1].position= mx-sx,my
		self.vertArray[3].position= mx+sx,my
		self.vertArray[5].position= mx,my-sy
		self.vertArray[7].position= mx,my+sy

		target.draw(self.vertArray,states)
