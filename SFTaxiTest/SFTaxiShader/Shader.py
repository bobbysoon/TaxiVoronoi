#!/usr/bin/python

from sfml import sf

from os.path import split

def fileWrite(fp, text):
	h=open(fp,'wt')
	if h:		h.write(text);h.close()
	else:		raise ValueError('fileWrite failed')

def Shader(P):
	global sText,shader
	sText='''
	#version 120

	#define N %i
	vec2 P[N] = vec2[](%s);

	uniform vec2 iResolution;

	vec3 hue(float h, float s) {
		float v=1.0;
		if (s==0.0) return vec3(v);
		int i = int(floor(h*6.0));
		float f = (h*6.)-i;
		float p = (v*(1.-s));
		float q = (v*(1.-s*f));
		float t = (v*(1.-s*(1.-f)));
		i= int(mod(i,6));
		if (i == 0) return vec3(v, t, p);
		if (i == 1) return vec3(q, v, p);
		if (i == 2) return vec3(p, v, t);
		if (i == 3) return vec3(p, q, v);
		if (i == 4) return vec3(t, p, v);
		if (i == 5) return vec3(v, p, q);
	}

	void main() {
		float region=-1, dist;
		float minDistance = length(iResolution);
		vec2 minPos;

		for(int i=0; i<N; i++) {
			vec2 pos = P[i];
			dist = abs(pos.x - gl_TexCoord[0].x) + abs(pos.y - gl_TexCoord[0].y);

			if(dist <= minDistance) {
				minPos= pos;
				minDistance = dist;
				region = float(i+1) / float(N+1);
			}
		}

		float H= int(sqrt(N));
		gl_FragColor = vec4(hue(region*N/H,region) , 1.0);
	}'''%(len(P),( ', '.join(['vec2(%f,%f)'%(x,y) for x,y in P]) ))

	fileWrite('renderTexture.glsl',sText)

	nullVertShader=b'''#version 120
	void main() {
		gl_Position=gl_ProjectionMatrix*gl_ModelViewMatrix*gl_Vertex;
		gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;
		gl_FrontColor = gl_Color;
	}'''


	shader= sf.Shader.from_memory(nullVertShader, sText)
	return shader


