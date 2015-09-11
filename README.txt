TaxiVoronoi generates a polygonal representation of a voronoi diagram in manhattan metric

sfTest.py requires python-sfml.

The bottleneck is in the border intersects, so I took a crack at cythonizing that part.
Run TaxiVoronoi/TaxiVoronoi/Intersect_cython/comp to compile Intersect.so.
This has greatly improved speed, with only a few variable type declarations.

So far, only tested in a (0,0),(1,1) range of points.
Might require Poly.epsilon adjustment for larger/smaller scale, if verts aren't welding between polies. Currently it's 1e-04. 

It will fail if any two supplied centroids are horizontal, vertical, or a 45 degree diagonal to each other. 
With the RandomPointGrid settings where they are (in sfTest.py), this happens frequently.

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


note: This can be done faster. I'm seeing good results so far in a process surmized as:
(i hope you like python)
(P= the centroids)
determine bounds of P: bounds= 100+% of min & max of P
create 4 temporary centroids, TP
for p in P:
	adjust TP so that they're mirroring p across the boundary lines, top,bottom,left,right
	PP=P+TP
	others= manhattan-distance from p sorted list of centroids in PP who aren't p
	notClosed=True
	B= empty list
	while list of others isn't empty, and notClosed:
		pp= others.pop(the next nearest to p)
		b= Border(p,pp)
		for bb in B:
			v= intersect(b,bb)
			if v:
				t= Trisect(v,PP)
				if t:
					centroids in t are adjacent each other
					v is a vert of boundary of each centroid in t
					note that b and bb have each intersected another boundary once or twice

		add b to B
		if all borders in B have trisected twice, notClosed=False


Many operations are the same in reverse. Border(p1,p2)==Border(p2,p1). Intersect(b1,b2)==Intersect(b2,b1)


Trisect test is d2-d1<epsilon and d3-d2<epsilon, for dists d1,d2,d3 from point, testing all points of PP, which includes the temporary boundary centroids. I been using epsilon=1e-04, with P=rnd(1024.0)
Trisect can return the three centroid regions it divides. They neighbor each other. You might note a neighbor of None or NILL for a temporary centroid


Next is to add the points of the diagonal line segment of each border which passes a bisect test, similar to the trisect test
Sequencing each centroid's polie's verts is simple to do by sorting the angle from centroid to vert. "Winding order", clockwise or ccw, can also be tested to see if you need to reverse a poly, for collision or hardware rendering or whatever.

if you need to know which vert pair of a notClosed poly is the opening, bisect test (v1+v2)/2. 
