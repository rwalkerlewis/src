[sfbeamsteer]
Cat:    RSF/user/browaeys
Desc:   Beam steering for 2D surface array
DocCmd: sfbeamsteer | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dpx float  -   -  		px sampling (if mode=y). 
Param:  dpy float  -   -  		py sampling (if mode=y). 
Param:  mode enum-bool  -  y 		if n, beams computed as a function of apparent slowness and azimuth angle. 
Param:  npx int  -   -  		number of px values (if mode=y). 
Param:  npy int  -   -  		number of py values (if mode=y). 
Param:  opx float  -   -  		px origin (if mode=y) 
Param:  opy float  -   -  		py origin (if mode=y) 
Param:  xref float  -   -  		x coordinate where beams are computed 
Param:  yref float  -   -  		y coordinate where beams are computed 

