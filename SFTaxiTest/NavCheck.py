from math import *
from sfml import sf
Key = sf.Keyboard
KeyPressed = Key.is_key_pressed

deg2rad=6.283185/360.0

def rotateViewAroundPoint(w,degrees,p):
	r= degrees*deg2rad ; x,y = w.view.center-p
	w.view.center= p+(x*cos(r)-y*sin(r),y*cos(r)+x*sin(r))
	w.view.rotate( degrees )

def zoomViewOnPoint(w,z,p):
	w.view.center= p+(w.view.center-p)*z
	w.view.zoom(z)

ZOOMSTEP=2.0
mouseCoord=None
def checkForNavEvents(w,e,mPos):
	global mouseCoord
	if type(e) is sf.CloseEvent or (type(e) is sf.KeyEvent and e.code == Key.ESCAPE):
		w.close()
	elif type(e) is sf.MouseWheelEvent and e.delta:
		zoomViewOnPoint(w, (7./8.) if e.delta>0 else (8./7.) ,mPos)
	elif type(e) is sf.MouseButtonEvent and e.button==sf.Mouse.MIDDLE:
		mouseCoord= mPos if e.pressed else None
	elif type(e) is sf.MouseMoveEvent and mouseCoord:
		dx,dy=mouseCoord-mPos
		w.view.move(dx,dy)


def checkNavKeys(w,tDelta,mPos):
	if KeyPressed(Key.HOME):
		r=w.view.rotation
		if r>180: r-=360
		w.view.rotate(-r*tDelta*8)

		z=1.0-w.view.size.y
		w.view.zoom( ZOOMSTEP/(ZOOMSTEP-tDelta*z*8))

		dx,dy= (sf.Vector2(.5,.5)-w.view.center) * tDelta * 8
		w.view.move(dx,dy)

	if KeyPressed(Key.Q):	rotateViewAroundPoint(w,-90*tDelta,mPos)
	if KeyPressed(Key.E):	rotateViewAroundPoint(w, 90*tDelta,mPos)

	if KeyPressed(Key.PAGE_UP):		zoomViewOnPoint(w, (ZOOMSTEP-tDelta)/ZOOMSTEP ,mPos)
	if KeyPressed(Key.PAGE_DOWN):	zoomViewOnPoint(w, ZOOMSTEP/(ZOOMSTEP-tDelta) ,mPos)

	dx,dy=0,0
	if KeyPressed(Key.A):	dx=-1
	if KeyPressed(Key.D):	dx= 1
	if KeyPressed(Key.W):	dy=-1
	if KeyPressed(Key.S):	dy= 1
	if dx or dy:
		scale=min(list(w.view.size))
		d=dx,dy
		r= [( 0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)].index(d)
		r= r*45-w.view.rotation
		a= r*deg2rad
		v= sf.Vector2(sin(a),cos(a))
		w.view.center+= v*scale*tDelta/4.0
