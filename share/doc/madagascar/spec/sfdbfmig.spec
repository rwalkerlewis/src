[sfdbfmig]
Cat:    RSF/user/aklokov
Desc:   
DocCmd: sfdbfmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing piFile data)
Port:   stdout rsf w req 	RSF standard output (containing resFile data)
Param:  dt float  -   -  		time-range for point detection 
LDesc:  (defaults to: 0.008f)
Param:  dx float  -   -  		x-range for point detection 
LDesc:  (defaults to: xStep)
Param:  esct string  -   -  		escape-time file (auxiliary input file name)
Param:  escx string  -   -  		escape-positions file (auxiliary input file name)
Param:  isAA enum-bool  -  y 		if y, apply anti-aliasing 
Param:  ixd float  -   -  		step in positions (in meters) 
LDesc:  (defaults to: xStep)
Param:  ixn int  -   -  		number of imaged positions 
LDesc:  (defaults to: xNum)
Param:  ixo float  -   -  		first imaged position (in meters) 
LDesc:  (defaults to: xStart)
Param:  izd float  -   -  		step in depth (in meters) 
LDesc:  (defaults to: zStep)
Param:  izn int  -   -  		number of imaged depth samples 
LDesc:  (defaults to: zNum)
Param:  izo float  -   -  		first imaged depth (in meters) 
LDesc:  (defaults to: zStart)
Param:  pj int  -  1 		jump in points 
Param:  ppd float  -   -  		step in processed partial images 
LDesc:  (defaults to: pStep)
Param:  ppn int  -   -  		number of processed partial images 
LDesc:  (defaults to: pNum)
Param:  ppo float  -   -  		first processed partial image 
LDesc:  (defaults to: pStart)
Param:  sd float  -   -  		step in scattering-angles 
LDesc:  (defaults to: 1.f)
Param:  sn int  -  1 		number of scattering-angles 
Param:  so float  -   -  		first scattering-angle 
LDesc:  (defaults to: 0.f)
Param:  xapert float  -   -  		migration aperture size 
LDesc:  (defaults to: xNum * xStep)
Param:  xlim float  -   -  		maximum distance between depth-line points 
LDesc:  (defaults to: 2 * xStep)

