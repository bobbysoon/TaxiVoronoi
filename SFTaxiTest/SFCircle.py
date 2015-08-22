from sfml import sf

class SFCircle(sf.Drawable):
	def __init__(self, oc=sf.Color.WHITE , ic=sf.Color.TRANSPARENT ):
		sf.Drawable.__init__(self)
		self.circle= sf.CircleShape()
		self.circle.outline_color = oc
		self.circle.fill_color = ic
	def setScale(self,scale):
		self.circle.radius=scale
		self.circle.outline_thickness=scale/2
		self.circle.origin=scale,scale
	def draw(self, target,states, pos=None):
		if pos: self.circle.position = pos
		target.draw(self.circle,states)

