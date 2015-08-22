from sfml import sf
from sys import argv

def Window():
	window = sf.RenderWindow( sf.VideoMode(800,600), argv[0] )
	wd,ht=window.size ; window.view.size = 1.5,1.5*float(ht)/wd ; window.view.center = .5,.5
	return window
