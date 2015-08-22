from sfml import sf

def VertexArray(poly, primitiveType=sf.PrimitiveType.POINTS, col=sf.Color.WHITE):
	va= sf.VertexArray( primitiveType , len(poly) )
	for i in range(len(poly)):	va[i].position= poly[i]
	if col:
		if type(col) is list:
			for i in range(len(poly)):	va[i].color= col[i]
		else:
			for i in range(len(poly)):	va[i].color= col
	return va
