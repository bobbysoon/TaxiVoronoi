TaxiVoronoi generates a polygonal representation of a voronoi diagram in manhattan metric

polies,verts = TaxiVoronoi(centroids)
	centroids:	list of 2d points
	polies: list of Poly
	verts: list of 2d points

Poly:
	centroid
	neighbors:	list of Poly - one per adjacent poly
	neighborIndices: list of indices of polies returned by TaxiVoronoi
	verts: list of indices of verts returned by TaxiVoronoi
	borders: list of Border - one per neighbor
	isClosed: boolean - outer polies wont be

	polies are wound counter-clockwise by default. Poly.WindingOrderUsed=Poly.clockwise will reverse them. So will poly.reverse().
