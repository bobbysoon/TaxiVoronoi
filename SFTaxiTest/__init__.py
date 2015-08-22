#from G import *
from sfml import sf
from Window import *
from MouseCursor import *
from NavCheck import *
from SFTaxiShader import *
from SFObjects import *


def SFTaxiTest(polies,verts):
	sfTaxiShader= SFTaxiShader([poly.centroid for poly in polies])
	window= Window()
	mouseCursor= MouseCursor(window)

	sfObjects= SFObjects(polies,verts)

	clickPos=None ; clock = sf.Clock()
	while window.is_open:
		tDelta= clock.restart().seconds

		sfObjects.setScale(window.view.size.x/window.size.x)

		window.clear()
		#window.draw(sfTaxiShader)
		sfTaxiShader.quad.align(window)
		sfObjects.quadCorners = sfTaxiShader.quad.corners()
		sfObjects.updateRays(sfTaxiShader.corners())
		window.draw(sfObjects)
		window.draw(mouseCursor)
		window.display()

		checkNavKeys(window,tDelta,mouseCursor.pos)
		for event in window.events:
			if		type(event) is sf.CloseEvent:			window.close()
			elif	type(event) is sf.MouseButtonEvent and event.pressed:
				if event.button==sf.Mouse.LEFT:			sfObjects.clickedAt(mouseCursor.pos)
				else:	checkForNavEvents(window,event,mouseCursor.pos)
			elif	type(event) is sf.KeyEvent and event.pressed:
				if		event.code == sf.Keyboard.ESCAPE: window.close()
				elif	event.code == sf.Keyboard.P:	sfObjects.clickedAt= selectPoly
				elif	event.code == sf.Keyboard.I:	sfObjects.clickedAt= selectIntersect
				else:	checkForNavEvents(window,event,mouseCursor.pos)
			else:	checkForNavEvents(window,event,mouseCursor.pos)


