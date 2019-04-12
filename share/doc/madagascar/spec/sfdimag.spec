[sfdimag]
Cat:    RSF/system/seismic
Desc:   Diffraction imaging in the plane-wave domain
DocCmd: sfdimag | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing scan data)
Param:  dv float  -   -  		
Param:  extend int  -  4 		trace extension 
Param:  mute int  -  12 		mute zone 
Param:  nb int  -  2 		semblance averaging 
Param:  nv int  -   -  		
Param:  semblance enum-bool  -  n 		if y, compute semblance; if n, stack 
Param:  str float  -  0. 		maximum stretch allowed 
Param:  v0 float  -   -  		
Param:  x0 float  -   -  		

