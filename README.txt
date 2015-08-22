sfTest.py requires python-sfml.

TaxiVoronoi generates a polygonal representation of a voronoi diagram in manhattan metric

So far, only tested in a (0,0),(1,1) range of points.
Might require Poly.epsilon adjustment for larger/smaller scale. Currently it's 1e-04. 

polies,verts = TaxiVoronoi(centroids)
	centroids:	list of 2d points, aka sites, also centroids
	polies: list of Poly
	verts: list of 2d verts. Adjacent polies index the same verts.

Poly:
	centroid
	neighbors:	list of Poly - one per adjacent poly
	neighborIndices: list of indices of polies returned by TaxiVoronoi
	verts: list of indices of verts returned by TaxiVoronoi
	borders: list of Border - one per neighbor
	isClosed: boolean - outer polies wont be

	polies are wound counter-clockwise by default. Reverse them with
		Poly.WindingOrderUsed=Poly.clockwise or poly.reverse().
