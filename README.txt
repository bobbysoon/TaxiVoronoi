TaxiVoronoi generates a polygonal representation of a voronoi diagram in manhattan metric

sfTest.py requires python-sfml.

The bottleneck is in the border intersects, so I took a crack at cythonizing that part.
Run TaxiVoronoi/TaxiVoronoi/Intersect_cython/comp to compile Intersect.so.
This has greatly improved speed, with only a few variable type declarations.

So far, only tested in a (0,0),(1,1) range of points.
Might require Poly.epsilon adjustment for larger/smaller scale, if verts aren't welding between polies. Currently it's 1e-04. 

It will fail if any two supplied centroids are horizontal, vertical, or a 45 degree diagonal to each other. 

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
		isClosed= borders[0][0]==borders[-1][-1]
		a closed poly's 1st and last are duplicate indices

	polies are wound counter-clockwise by default. Reverse them with
		Poly.WindingOrderUsed=Poly.clockwise or poly.reverse().

Border:
	axis: (+-1,0) or (0,+-1) or None - horizontal, vertical, or as of yet unhandled scenario
	lines: [ray,segment,ray]
	seg: the afforementioned segment
	verts: much like Poly.verts

	a border's rays who an open vert of a non-closed poly lies on could be used to complete it's representation
