[sfvsptmigda]
Cat:    RSF/user/aklokov
Desc:   3D time scattering-angle Kirchhoff migration for VSP data
DocCmd: sfvsptmigda | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile data)
Port:   stdout rsf w req 	RSF standard output (containing imageFile data)
Param:  axis2label int  -  0 		0 - shot; 1 - cmp; 2 - receiver 
Param:  cig string  -   -  		output file containing CIGs in the surface-offset domain (auxiliary output file name)
Param:  dag string  -   -  		output file containing CIGs in the dip-angle domain (auxiliary output file name)
Param:  dipd float  -   -  		step in dip-angle 
LDesc:  (defaults to: 1.f)
Param:  dipn int  -  1 		number of dip-angles 
Param:  dipo float  -   -  		first dip-angle 
LDesc:  (defaults to: 0.f)
Param:  hmign int  -   -  		number of migrated offsets 
LDesc:  (defaults to: dp.hNum)
Param:  is3d enum-bool  -  n 		if y, apply 3D migration 
Param:  isAA enum-bool  -  y 		if y, apply anti-aliasing 
Param:  isDipAz enum-bool  -  y 		if y, apply dip/azimuth mode; if n, apply inline/crossline angle mode 
Param:  iscatd float  -   -  		scattering-angle increment (in degree) 
LDesc:  (defaults to: 2 * gp.dipStep)
Param:  iscatn int  -  1 		number of scattering-angles 
Param:  iscato float  -   -  		first scattering-angle (in degree) 
LDesc:  (defaults to: 0.f)
Param:  itd float  -   -  		step in imaged times  (in ms) 
LDesc:  (defaults to: dp.zStep)
Param:  itn int  -   -  		number of imaged times 
LDesc:  (defaults to: dp.zNum)
Param:  ito float  -   -  		first imaged time (in ms) 
LDesc:  (defaults to: dp.zStart)
Param:  ixd float  -   -  		step in imaged inlines 
LDesc:  (defaults to: dp.xStep)
Param:  ixn int  -   -  		number of imaged inlines 
LDesc:  (defaults to: dp.xNum)
Param:  ixo float  -   -  		first imaged inline 
LDesc:  (defaults to: dp.xStart)
Param:  iyd float  -   -  		step in imaged crosslines 
LDesc:  (defaults to: dp.yStep)
Param:  iyn int  -   -  		number of imaged crosslines 
LDesc:  (defaults to: rp.is3D ? vp.yNum : 1)
Param:  iyo float  -   -  		first imaged crossline 
LDesc:  (defaults to: dp.yStart)
Param:  semb string  -   -  		output file containing semblance measure of CIGs stacking (auxiliary output file name)
Param:  sembWindow int  -  11 		vertical window for semblance calculation (in samples) 
Param:  vel string  -   -  		velocity model file (velocity in m/s) (auxiliary input file name)

